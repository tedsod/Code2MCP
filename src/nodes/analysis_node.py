# Analysis Node - Use gitingest, LLM, and DeepWiki to analyze repository structure
from __future__ import annotations
import os
import json
import re
from typing import Dict, Any, List
from ..utils import setup_logging, get_llm_service, write_file
from ..tools.gitingest_client import GitingestClient
from ..tools.deepwiki_client import get_deepwiki_client

logger = setup_logging()

def _scan_python_packages(root_dir: str) -> List[str]:
    logger.info(f"Starting Python package scan, root directory: {root_dir}")
    packages: List[str] = []
    try:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            rel = os.path.relpath(dirpath, root_dir)
            if rel.count(os.sep) > 2:
                continue
            if "__init__.py" in filenames:
                pkg = rel.replace(os.sep, ".") if rel != "." else ""
                if pkg:
                    packages.append(pkg)
        return sorted(list(set(packages)))
    except Exception as e:
        logger.error(f"Error occurred while scanning Python packages: {e}")
        import traceback
        logger.error(f"Detailed error information: {traceback.format_exc()}")
        return []


def _scan_entry_points(working_dir: str) -> Dict[str, Any]:
    entry_points = {"imports": [], "cli": [], "modules": []}
    
    setup_py = os.path.join(working_dir, "setup.py")
    if os.path.exists(setup_py):
        try:
            with open(setup_py, 'r', encoding='utf-8') as f:
                content = f.read()
            
            matches = re.findall(r'console_scripts.*?\[(.*?)\]', content, re.DOTALL)
            for match in matches:
                scripts = re.findall(r'["\']([^"\']+)=([^"\']+)["\']', match)
                for script_match in scripts:
                    if len(script_match) == 2:
                        script_name, module_path = script_match
                        entry_points["cli"].append({
                            "name": script_name,
                            "module": module_path,
                            "type": "console_script"
                        })
        except Exception as e:
            logger.error(f"Failed to parse setup.py: {e}")
    
    pyproject_toml = os.path.join(working_dir, "pyproject.toml")

    if os.path.exists(pyproject_toml):

        try:
            with open(pyproject_toml, 'r', encoding='utf-8') as f:
                content = f.read()
            logger.info(f"pyproject.toml file size: {len(content)} characters")
            
            script_patterns = [
                r'\[project\.scripts\]\s*\n(.*?)(?=\n\[|\n$)', 
                r'\[tool\.poetry\.scripts\]\s*\n(.*?)(?=\n\[|\n$)'
            ]
            
            for pattern_idx, pattern in enumerate(script_patterns):
                matches = re.findall(pattern, content, re.DOTALL)
                
                for match_idx, match in enumerate(matches):
                    scripts = re.findall(r'([^=]+)\s*=\s*["\']([^"\']+)["\']', match)
                    
                    for script_idx, script_match in enumerate(scripts):
                        if len(script_match) == 2:
                            script_name, module_path = script_match
                        else:
                            continue
                        entry_points["cli"].append({
                            "name": script_name.strip(),
                            "module": module_path.strip(),
                            "type": "pyproject_script"
                        })
        except Exception as e:
            logger.error(f"Failed to parse pyproject.toml: {e}")
            import traceback
            logger.error(f"Detailed error information: {traceback.format_exc()}")
    
    return entry_points


def _analyze_with_llm(llm_service, repo_url: str, summary: Dict[str, Any], packages: List[str], entry_points: Dict[str, Any], deepwiki_analysis: Dict[str, Any]) -> Dict[str, Any]:
    if not llm_service:
        logger.warning("LLM service not available, using basic analysis")
        return _basic_analysis(packages, entry_points)
    
    try:
        logger.info(f"Summary size: {len(json.dumps(summary, ensure_ascii=False))} characters")
        
        deepwiki_url = repo_url.replace("github.com", "deepwiki.com") if "github.com" in repo_url else repo_url
        
        deepwiki_info = ""
        if deepwiki_analysis.get("success") and deepwiki_analysis.get("analysis"):
            deepwiki_info = f"""
DeepWiki Analysis Results:
{deepwiki_analysis.get("analysis", "")}
"""
        elif deepwiki_analysis.get("status") == "failed":
            deepwiki_info = f"""
DeepWiki Analysis Failed: {deepwiki_analysis.get("error", "Unknown error")}
"""
        else:
            deepwiki_info = """
DeepWiki Analysis: Skipped or not enabled
"""

        prompt = f"""
Please analyze the following code repository, identify the most suitable MCP plugin implementation strategy:

Original Repository URL: {repo_url}
DeepWiki Analysis URL: {deepwiki_url}

Gitingest Summary:
{json.dumps(summary, indent=2, ensure_ascii=False)}

Python Package Structure:
{json.dumps(packages, indent=2, ensure_ascii=False)}

Identified Entry Points:
{json.dumps(entry_points, indent=2, ensure_ascii=False)}

{deepwiki_info}

Please analyze and output a detailed JSON analysis result, including:

1. Core Function Module Identification
2. List of importable functions/classes
3. CLI Command Identification
4. Dependency Analysis
5. Minimal Intrusion Strategy Suggestions

Important: The scanned Python package paths are accurate, please analyze strictly according to these paths.

Output Format:
{{
    "core_modules": [
        {{
            "package": "Full package path scanned",
            "module": "Specific module name", 
            "functions": ["Function1", "Function2"],
            "classes": ["Class1", "Class2"],
            "description": "Function description"
        }}
    ],
    "cli_commands": [
        {{
            "name": "Command name",
            "module": "Module path",
            "description": "Function description"
        }}
    ],
    "import_strategy": {{
        "primary": "Primary import strategy (import/cli/blackbox)",
        "fallback": "Fallback strategy",
        "confidence": 0.8
    }},
    "dependencies": {{
        "required": ["Dependency1", "Dependency2"],
        "optional": ["Optional dependency1"]
    }},
    "risk_assessment": {{
        "import_feasibility": 0.8,
        "intrusiveness_risk": "low/medium/high",
        "complexity": "simple/medium/complex"
    }}
}}

Note: The package field must use the full scanned package path, do not simplify or modify it. Keep the original package path.
"""
        
        response = llm_service.invoke(prompt)
        
        try:
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                analysis_result = json.loads(json_match.group())
                logger.info("LLM analysis completed")
                return analysis_result
            else:
                logger.warning("JSON format not found in LLM response")
                return _basic_analysis(packages, entry_points)
        except json.JSONDecodeError as e:
            logger.warning(f"LLM response JSON parsing failed: {e}")
            return _basic_analysis(packages, entry_points)
            
    except Exception as e:
        logger.warning(f"LLM analysis failed: {e}")
        return _basic_analysis(packages, entry_points)


def _basic_analysis(packages: List[str], entry_points: Dict[str, Any]) -> Dict[str, Any]:
    core_modules = []
    if packages:
        top_package = min(packages, key=lambda p: p.count("."))
        core_modules.append({
            "package": top_package,
            "module": top_package,
            "functions": ["main"],
            "classes": [],
            "description": "Main function module"
        })
    
    return {
        "core_modules": core_modules,
        "cli_commands": entry_points.get("cli", []),
        "import_strategy": {
            "primary": "import" if packages else "cli" if entry_points.get("cli") else "blackbox",
            "fallback": "cli" if entry_points.get("cli") else "blackbox",
            "confidence": 0.5
        },
        "dependencies": {
            "required": [],
            "optional": []
        },
        "risk_assessment": {
            "import_feasibility": 0.5 if packages else 0.2,
            "intrusiveness_risk": "low" if packages else "medium",
            "complexity": "simple"
        }
    }

def analysis_node(state: Dict[str, Any]) -> Dict[str, Any]:

    logger.info("=== Starting analysis node ===")
    
    repo = state.get("repository", {})
    repo_url = repo.get("url")
    repo_root = repo.get("local_paths", {}).get("repo_root")
    
    logger.info(f"Repository URL: {repo_url}")
    logger.info(f"Repository root directory: {repo_root}")
    
    if not (repo_url and repo_root and os.path.isdir(repo_root)):
        logger.error("Missing repo_url or repo_root path")
        state.setdefault("errors", []).append({
            "node": "AnalysisNode",
            "type": "InvalidInput",
            "message": "Missing repo_url or repo_root path",
            "action_taken": "abort"
        })
        state["status"] = "failed"
        state["workflow_status"] = "failed"
        return state

    summary: Dict[str, Any] = {}
    try:
        logger.info("Starting gitingest client call...")
        client = GitingestClient()
        logger.info("gitingest client created successfully")
    
        summary = client.preprocess_repository_sync(repo_url)
        if summary is None:
            summary = {"status": "failed", "error": "gitingest preprocess returned None"}
            logger.warning("gitingest preprocess failed, returned None")
        logger.info("gitingest preprocess completed")
    except Exception as e:
        logger.error(f"gitingest preprocess failed: {e}")
        import traceback
        logger.error(f"Detailed error information: {traceback.format_exc()}")
        state.setdefault("warnings", []).append(f"gitingest preprocess failed: {e}")

    packages = _scan_python_packages(repo_root)
    entry_points = _scan_entry_points(repo_root)
    source_dir = os.path.join(repo_root, "source")
    dependencies = {
        "has_environment_yml": (
            os.path.exists(os.path.join(repo_root, "environment.yml")) or
            os.path.exists(os.path.join(source_dir, "environment.yml"))
        ),
        "has_requirements_txt": (
            os.path.exists(os.path.join(repo_root, "requirements.txt")) or
            os.path.exists(os.path.join(source_dir, "requirements.txt"))
        ),
        "pyproject": (
            os.path.exists(os.path.join(repo_root, "pyproject.toml")) or
            os.path.exists(os.path.join(source_dir, "pyproject.toml"))
        ),
        "setup_cfg": (
            os.path.exists(os.path.join(repo_root, "setup.cfg")) or
            os.path.exists(os.path.join(source_dir, "setup.cfg"))
        ),
        "setup_py": (
            os.path.exists(os.path.join(repo_root, "setup.py")) or
            os.path.exists(os.path.join(source_dir, "setup.py"))
        ),
    }
    logger.info(f"Dependency file check results: {dependencies}")

    deepwiki_analysis = {"status": "skipped"}
    deepwiki_model = state.get("options", {}).get("deepwiki_model")
    if deepwiki_model:
        try:
            model = deepwiki_model
            deepwiki_client = get_deepwiki_client(model=model)
            repo_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")
            deepwiki_analysis = deepwiki_client.analyze_repository(repo_url, repo_name)
            logger.info("DeepWiki analysis completed")
        except Exception as e:
            logger.warning(f"DeepWiki analysis failed: {e}")
            state.setdefault("warnings", []).append(f"DeepWiki analysis failed: {e}")
            deepwiki_analysis = {"status": "failed", "error": str(e)}
    else:
        logger.info("DeepWiki analysis skipped (model not configured)")
    
    logger.info("Starting LLM service...")
    llm_service = get_llm_service()
    logger.info("LLM service obtained")
    
    logger.info("Starting LLM analysis...")
    # Pass DeepWiki analysis results to LLM
    llm_analysis = _analyze_with_llm(llm_service, repo_url, summary, packages, entry_points, deepwiki_analysis)
    logger.info("LLM analysis completed")

    analysis_result = {
        "summary": summary,
        "structure": {"packages": packages},
        "dependencies": dependencies,
        "entry_points": entry_points,
        "llm_analysis": llm_analysis,
        "deepwiki_analysis": deepwiki_analysis,
        "deepwiki_options": {
            "enabled": bool(deepwiki_model),
            "model": deepwiki_model,
        },
        "risk": llm_analysis.get("risk_assessment", {
            "import_feasibility": 0.5,
            "intrusiveness_risk": "low",
            "complexity": "simple"
        })
    }

    mcp_output_dir = os.path.join(repo_root, "mcp_output")
    os.makedirs(mcp_output_dir, exist_ok=True)
    
    analysis_json_path = os.path.join(mcp_output_dir, "analysis.json")
    try:
        write_file(analysis_json_path, json.dumps(analysis_result, ensure_ascii=False, indent=2))
        logger.info(f"Analysis results saved to: {analysis_json_path}")
    except Exception as e:
        logger.warning(f"Failed to save analysis.json: {e}")
        state.setdefault("warnings", []).append(f"Failed to save analysis.json: {e}")

    state["analysis"] = analysis_result
    state["status"] = "running"
    state["workflow_status"] = state.get("workflow_status", "running")
    return state

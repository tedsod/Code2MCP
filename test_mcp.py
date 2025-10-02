#!/usr/bin/env python
"""Quick harness for poking at the exchange-service MCP module."""
import asyncio
import importlib.util
import json
from pathlib import Path
from typing import Any, Dict, Optional

from fastmcp import Client, FastMCP


async def call_tool(
    client: Client,
    name: str,
    payload: Optional[Dict[str, Any]],
) -> None:
    result = await client.call_tool(name, payload or {})
    print("result.is_error:", result.is_error)
    data = result.data or result.structured_content
    if isinstance(data, dict) and "result" in data:
        success = data.get("success")
        error = data.get("error")
        if success:
            print("result.value:", json.dumps(data["result"], indent=2, sort_keys=True))
        else:
            print("result.error:", error)
    elif data is not None:
        print(json.dumps(data, indent=2, sort_keys=True))
    else:
        print(result.content)


def resolve_transport(module_spec: str) -> FastMCP | Path | str:
    """Return something Client() understands from a spec like path or path:object."""
    if ":" not in module_spec:
        # plain path or URL – let Client/infer_transport handle it
        return module_spec

    path_str, attr = module_spec.split(":", 1)
    module_path = Path(path_str).resolve()
    if not module_path.exists():
        raise FileNotFoundError(f"Module file not found: {module_path}")

    spec = importlib.util.spec_from_file_location("mcp_module", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {module_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]

    try:
        server = getattr(module, attr)
    except AttributeError as exc:
        raise AttributeError(f"Module '{module_path}' has no attribute '{attr}'") from exc

    if not isinstance(server, FastMCP):
        raise TypeError(
            f"Attribute '{attr}' in '{module_path}' is not a FastMCP server instance"
        )
    return server


MODULE_SPEC = "workspace/exchange-api/mcp_output/mcp_plugin/mcp_service.py:mcp"
# test_mcp.py
TOOL_NAME = "get_all_currencies"
#TOOL_PAYLOAD = {"base_currency": "USD", "target_currency": "EUR"}
TOOL_PAYLOAD = None



async def main() -> None:
    transport = resolve_transport(MODULE_SPEC)
    client = Client(transport)
    async with client:
        await call_tool(client, TOOL_NAME, TOOL_PAYLOAD)


if __name__ == "__main__":
    asyncio.run(main())

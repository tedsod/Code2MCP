import React, { useState } from "react";
import { motion } from "framer-motion";
import { Github, Sparkles, ArrowRight, TerminalSquare, ShieldCheck, Rocket, CheckCircle2, Link as LinkIcon } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

// Minimal, single-file homepage for an MCP auto-generator service.
// - TailwindCSS for styling
// - shadcn/ui for Button & Card
// - framer-motion for subtle animations
// Drop this into a Next.js/React app as the default export page.

export default function HomePage() {
  const [repoUrl, setRepoUrl] = useState("");
  const [status, setStatus] = useState({ type: "idle" });
  const [result, setResult] = useState(null);

  const isValidGithubUrl = (url) => {
    // Accepts https://github.com/owner/repo( .git ) and optional paths
    const re = /^https?:\/\/(www\.)?github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+(\.git)?(\/)?$/;
    return re.test(url.trim());
  };

  const handleGenerate = async () => {
    setResult(null);
    if (!isValidGithubUrl(repoUrl)) {
      setStatus({ type: "error", message: "Enter a valid GitHub repository URL (e.g., https://github.com/owner/repo)." });
      return;
    }
    setStatus({ type: "loading", message: "Scanning repository and generating MCP server…" });

    // TODO: Replace this mock with your real backend route (e.g., /api/generate)
    // The backend should:
    // 1) clone/scan the repo
    // 2) generate MCP schema/server artifacts
    // 3) optionally deploy and return an endpoint
    try {
      // Simulate network delay
      await new Promise((r) => setTimeout(r, 1400));
      const mock = {
        endpoint: "https://mcp.example.com/servers/abc123",
        serverId: "abc123",
        logs: [
          "Cloned repo",
          "Analyzed functions & CLI entrypoints",
          "Generated MCP schema",
          "Built server image",
          "Deployed to edge",
        ],
      };
      setResult(mock);
      setStatus({ type: "success", message: "MCP server generated successfully!" });
    } catch (e) {
      setStatus({ type: "error", message: "Something went wrong while generating the MCP server." });
    }
  };

  return (
    <div className="min-h-screen bg-white text-neutral-900">
      {/* Nav */}
      <header className="sticky top-0 z-40 w-full border-b bg-white/80 backdrop-blur">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3">
          <div className="flex items-center gap-2">
            <Sparkles className="h-5 w-5" />
            <span className="font-semibold">MCP Auto‑Gen</span>
          </div>
          <nav className="hidden gap-6 text-sm md:flex">
            <a href="#how" className="opacity-70 hover:opacity-100">How it works</a>
            <a href="#features" className="opacity-70 hover:opacity-100">Features</a>
            <a href="#examples" className="opacity-70 hover:opacity-100">Examples</a>
            <a href="#faq" className="opacity-70 hover:opacity-100">FAQ</a>
          </nav>
          <div className="flex items-center gap-2">
            <a href="https://github.com" target="_blank" rel="noreferrer" className="hidden md:block">
              <Button variant="outline" className="gap-2"><Github className="h-4 w-4"/> Star on GitHub</Button>
            </a>
            <Button
              className="gap-2"
              onClick={() => {
                const el = document.getElementById("repo-input");
                if (el) {
                  el.scrollIntoView({ behavior: "smooth", block: "center" });
                  if (el instanceof HTMLInputElement) {
                    el.focus();
                  }
                }
              }}
            >
              Try it
            </Button>
          </div>
        </div>
      </header>

      {/* Hero */}
      <section className="mx-auto max-w-6xl px-4 pt-16 pb-10">
        <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }}>
          <h1 className="text-balance text-4xl font-bold tracking-tight md:text-6xl">
            Turn any GitHub repo into an <span className="bg-gradient-to-r from-black to-neutral-500 bg-clip-text text-transparent">MCP server</span> — instantly.
          </h1>
          <p className="mt-4 max-w-2xl text-lg text-neutral-600">
            Paste a repository URL. We scan it, infer useful tools, and generate a ready-to-use MCP endpoint for your agents.
          </p>
        </motion.div>

        {/* Input Bar */}
        <motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.4, delay: 0.2 }} className="mt-8">
          <div className="mx-auto flex max-w-3xl items-center gap-2 rounded-2xl border p-2 shadow-sm">
            <LinkIcon className="ml-1 h-5 w-5 opacity-60"/>
            <input
              id="repo-input"
              value={repoUrl}
              onChange={(e) => setRepoUrl(e.target.value)}
              placeholder="https://github.com/owner/repo"
              className="w-full rounded-xl bg-transparent px-3 py-3 outline-none placeholder:text-neutral-400"
            />
            <Button onClick={handleGenerate} className="rounded-xl px-4">
              Generate MCP <ArrowRight className="ml-2 h-4 w-4" />
            </Button>
          </div>
          {/* Status line */}
          <div className="mx-auto mt-3 max-w-3xl min-h-6 text-sm">
            {status.type === "error" && (
              <div className="text-red-600">{status.message}</div>
            )}
            {status.type === "loading" && (
              <div className="animate-pulse text-neutral-600">{status.message}</div>
            )}
            {status.type === "success" && (
              <div className="text-emerald-600">{status.message}</div>
            )}
          </div>
        </motion.div>

        {/* Result Preview */}
        {result && (
          <motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.4, delay: 0.1 }} className="mx-auto mt-6 max-w-3xl">
            <Card className="rounded-2xl border-neutral-200">
              <CardContent className="p-5">
                <div className="flex items-center justify-between gap-4">
                  <div>
                    <div className="text-sm uppercase tracking-wide text-neutral-500">Deployed Endpoint</div>
                    <a href={result.endpoint} className="text-balance break-all text-base font-medium text-blue-600 hover:underline" target="_blank" rel="noreferrer">
                      {result.endpoint}
                    </a>
                  </div>
                  <span className="rounded-full bg-emerald-50 px-3 py-1 text-sm font-medium text-emerald-700">ID: {result.serverId}</span>
                </div>
                <div className="mt-4 rounded-xl bg-neutral-50 p-4">
                  <div className="mb-2 flex items-center gap-2 text-sm font-medium text-neutral-600">
                    <TerminalSquare className="h-4 w-4"/> Build Logs
                  </div>
                  <pre className="max-h-48 overflow-auto whitespace-pre-wrap text-sm text-neutral-800">{result.logs?.map(l => `• ${l}`).join("\n")}</pre>
                </div>
                <div className="mt-4 text-sm text-neutral-600">Use this endpoint in your agent’s MCP client to discover tools and call them securely.</div>
              </CardContent>
            </Card>
          </motion.div>
        )}
      </section>

      {/* How it works */}
      <section id="how" className="mx-auto max-w-6xl px-4 py-14">
        <div className="grid gap-6 md:grid-cols-3">
          <Step icon={<LinkIcon className="h-5 w-5"/>} title="Paste repo">
            Point us to your GitHub project. We handle cloning and static analysis.
          </Step>
          <Step icon={<Rocket className="h-5 w-5"/>} title="Generate tools">
            We infer useful functions, endpoints, and CLI commands to expose via MCP.
          </Step>
          <Step icon={<ShieldCheck className="h-5 w-5"/>} title="Deploy & secure">
            Get a versioned MCP server with auth, logs, and guardrails.
          </Step>
        </div>
      </section>

      {/* Features */}
      <section id="features" className="mx-auto max-w-6xl px-4 pb-14">
        <div className="grid gap-6 md:grid-cols-3">
          <Feature title="Consistent schema" desc="All tools expose the same MCP contract, so agents can discover & call them reliably."/>
          <Feature title="Language‑agnostic" desc="Python, Node, CLIs, microservices—wrap almost anything with no bespoke glue."/>
          <Feature title="Zero‑touch updates" desc="When your repo changes, your MCP server updates with versioning and rollback."/>
        </div>
      </section>

      {/* Examples */}
      <section id="examples" className="mx-auto max-w-6xl px-4 pb-16">
        <h2 className="text-2xl font-semibold">Examples</h2>
        <div className="mt-6 grid gap-6 md:grid-cols-2">
          <ExampleCard
            title="Weather API"
            repo="https://github.com/owner/weather"
            items={["GET /weather{city}", "tool: getCurrentWeather", "tool: forecast"]}
          />
          <ExampleCard
            title="Slack Bot"
            repo="https://github.com/owner/slack-bot"
            items={["tool: postMessage", "tool: createChannel", "tool: listUsers"]}
          />
        </div>
      </section>

      {/* FAQ */}
      <section id="faq" className="mx-auto max-w-6xl px-4 pb-24">
        <h2 className="text-2xl font-semibold">FAQ</h2>
        <div className="mt-6 space-y-4 text-neutral-700">
          <div>
            <div className="font-medium">Do I need a chat box to use this?</div>
            <p className="text-sm text-neutral-600">No. Paste a repo URL and click Generate. That’s it.</p>
          </div>
          <div>
            <div className="font-medium">What does the backend need?</div>
            <p className="text-sm text-neutral-600">An endpoint that accepts a GitHub URL, runs your Code2MCP pipeline, and returns a deployed endpoint + logs.</p>
          </div>
          <div>
            <div className="font-medium">Is this secure for private repos?</div>
            <p className="text-sm text-neutral-600">Use GitHub App/OAuth with least-privilege scopes; deploy servers inside your VPC and enable audit logs & RBAC.</p>
          </div>
        </div>
      </section>

      <footer className="border-t py-10">
        <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 px-4 md:flex-row">
          <div className="text-sm text-neutral-600">© {new Date().getFullYear()} MCP Auto‑Gen. All rights reserved.</div>
          <div className="flex items-center gap-4 text-sm">
            <a className="opacity-70 hover:opacity-100" href="#">Docs</a>
            <a className="opacity-70 hover:opacity-100" href="#">Privacy</a>
            <a className="opacity-70 hover:opacity-100" href="#">Terms</a>
          </div>
        </div>
      </footer>
    </div>
  );
}

function Step({ icon, title, children }) {
  return (
    <Card className="rounded-2xl border-neutral-200">
      <CardContent className="p-5">
        <div className="flex items-center gap-2 text-neutral-700">
          {icon}
          <div className="font-medium">{title}</div>
        </div>
        <p className="mt-2 text-sm text-neutral-600">{children}</p>
      </CardContent>
    </Card>
  );
}

function Feature({ title, desc }) {
  return (
    <Card className="rounded-2xl border-neutral-200">
      <CardContent className="p-5">
        <div className="flex items-center gap-2 text-neutral-700">
          <CheckCircle2 className="h-5 w-5"/>
          <div className="font-medium">{title}</div>
        </div>
        <p className="mt-2 text-sm text-neutral-600">{desc}</p>
      </CardContent>
    </Card>
  );
}

function ExampleCard({ title, repo, items }) {
  return (
    <Card className="rounded-2xl border-neutral-200">
      <CardContent className="p-5">
        <div className="flex items-center justify-between gap-4">
          <div className="text-lg font-medium">{title}</div>
          <a href={repo} target="_blank" rel="noreferrer" className="text-sm text-blue-600 hover:underline flex items-center gap-1"><Github className="h-4 w-4"/>View repo</a>
        </div>
        <ul className="mt-3 list-inside list-disc text-sm text-neutral-700">
          {items.map((it, i) => (<li key={i}>{it}</li>))}
        </ul>
      </CardContent>
    </Card>
  );
}

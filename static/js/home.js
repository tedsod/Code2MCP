const { useState } = React;

const MotionDiv = ({ children, initial, animate, transition, ...rest }) =>
  React.createElement("div", rest, children);

const createIcon = (paths, options = {}) => ({ className = "", size = 24, ...rest } = {}) =>
  React.createElement(
    "svg",
    {
      xmlns: "http://www.w3.org/2000/svg",
      viewBox: "0 0 24 24",
      width: size,
      height: size,
      fill: "none",
      stroke: options.stroke || "currentColor",
      strokeWidth: options.strokeWidth || 1.6,
      strokeLinecap: options.strokeLinecap || "round",
      strokeLinejoin: options.strokeLinejoin || "round",
      className,
      ...rest,
    },
    paths.map((attrs, index) => {
      const { tag, fill, stroke, ...pathProps } = attrs;
      return React.createElement(tag || "path", {
        key: index,
        fill: fill ?? "none",
        stroke: stroke ?? "currentColor",
        ...pathProps,
      });
    })
  );

const Sparkles = createIcon(
  [
    {
      d: "M12 3l2.3 5.7 6.2.5-4.8 3.7 1.6 5.8L12 16.6l-5.3 2.1 1.6-5.8-4.8-3.7 6.2-.5L12 3z",
      fill: "currentColor",
      stroke: "none",
    },
    {
      d: "M6 14.5l1 2.4 2.6.2-2 1.6.6 2.4L6 20.6l-2.2 1.5.6-2.4-2-1.6 2.6-.2L6 14.5z",
      fill: "currentColor",
      stroke: "none",
    },
    {
      d: "M18 5l.8 2 2 .2-1.5 1.1.5 2-1.8-1-1.8 1 .5-2-1.5-1.1 2-.2L18 5z",
      fill: "currentColor",
      stroke: "none",
    },
  ],
  { strokeWidth: 1.4 }
);

const Github = createIcon(
  [
    {
      d: "M12 2C6.477 2 2 6.484 2 12.017c0 4.423 2.865 8.18 6.839 9.504.5.091.682-.217.682-.482 0-.237-.009-.866-.014-1.699-2.782.605-3.369-1.34-3.369-1.34-.455-1.158-1.11-1.466-1.11-1.466-.908-.619.069-.607.069-.607 1.003.071 1.531 1.031 1.531 1.031.892 1.53 2.341 1.088 2.91.833.091-.647.35-1.088.636-1.338-2.22-.252-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.025A9.564 9.564 0 0 1 12 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.025 2.747-1.025.546 1.378.202 2.397.1 2.65.64.7 1.027 1.595 1.027 2.688 0 3.847-2.339 4.696-4.566 4.944.359.31.678.922.678 1.857 0 1.34-.012 2.421-.012 2.75 0 .268.18.58.688.482A10.019 10.019 0 0 0 22 12.017C22 6.484 17.523 2 12 2z",
      fill: "currentColor",
      stroke: "none",
    },
  ],
  { stroke: "none" }
);

const ArrowRight = createIcon([
  { d: "M5 12h14" },
  { d: "M13 8l4 4-4 4" },
]);

const TerminalSquare = createIcon(
  [
    { tag: "rect", x: 4, y: 4, width: 16, height: 16, rx: 2 },
    { d: "M8 9l3 3-3 3" },
    { d: "M12 15h4" },
  ],
  { strokeWidth: 1.5 }
);

const ShieldCheck = createIcon(
  [
    { d: "M12 3l6 3v4c0 4.5 -3.5 8.5 -6 9 -2.5 -.5 -6 -4.5 -6 -9V6l6-3z" },
    { d: "M9 12l2 2 4-4" },
  ],
  { strokeWidth: 1.5 }
);

const Rocket = createIcon(
  [
    {
      d: "M4.5 16.5c-1.5-.5-2.5-1.6-2.5-2.9 0-1 .6-1.9 1.5-2.4 2.5-1.4 4.4-3.3 5.8-5.8.5-.9 1.4-1.5 2.4-1.5 1.3 0 2.5 1 2.9 2.5l.7 2.5 2.5.7c1.5.4 2.5 1.6 2.5 2.9 0 1-.6 1.9-1.5 2.4-2.5 1.4-4.4 3.3-5.8 5.8-.5.9-1.4 1.5-2.4 1.5-1.3 0-2.5-1-2.9-2.5l-.7-2.5-2.5-.7z",
    },
    { d: "M8.5 14.5l3 3" },
    { d: "M9 9a3 3 0 1 1 6 0 3 3 0 0 1-6 0z" },
  ],
  { strokeWidth: 1.5 }
);

const CheckCircle2 = createIcon(
  [
    { d: "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z" },
    { d: "M8.5 12.5l2.5 2.5L16 10" },
  ],
  { strokeWidth: 1.5 }
);

const LinkIcon = createIcon(
  [
    {
      d: "M10.5 13.5a3.5 3.5 0 0 0 4.95 0l1.6-1.6a3.5 3.5 0 0 0-4.95-4.95l-.65.65",
    },
    {
      d: "M13.5 10.5a3.5 3.5 0 0 0-4.95 0l-1.6 1.6a3.5 3.5 0 0 0 4.95 4.95l.65-.65",
    },
  ],
  { strokeWidth: 1.5 }
);

const buttonBase =
  "inline-flex items-center justify-center gap-2 rounded-xl px-4 py-2 text-sm font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2";

const Button = ({ variant = "default", className = "", children, ...props }) => {
  const styles =
    variant === "outline"
      ? "border border-neutral-200 bg-white text-neutral-900 hover:bg-neutral-50"
      : "bg-neutral-900 text-white hover:bg-neutral-800";

  return React.createElement(
    "button",
    {
      className: `${buttonBase} ${styles} ${className}`.trim(),
      ...props,
    },
    children
  );
};

const Card = ({ className = "", children }) =>
  React.createElement(
    "div",
    {
      className: `rounded-2xl border border-neutral-200 bg-white shadow-sm ${className}`.trim(),
    },
    children
  );

const CardContent = ({ className = "", children }) =>
  React.createElement(
    "div",
    {
      className: `p-5 ${className}`.trim(),
    },
    children
  );

function Step({ icon, title, children }) {
  return React.createElement(
    Card,
    null,
    React.createElement(
      CardContent,
      null,
      React.createElement(
        "div",
        { className: "flex items-center gap-2 text-neutral-700" },
        icon,
        React.createElement("div", { className: "font-medium" }, title)
      ),
      React.createElement(
        "p",
        { className: "mt-2 text-sm text-neutral-600" },
        children
      )
    )
  );
}

function Feature({ title, desc }) {
  return React.createElement(
    Card,
    null,
    React.createElement(
      CardContent,
      null,
      React.createElement(
        "div",
        { className: "flex items-center gap-2 text-neutral-700" },
        React.createElement(CheckCircle2, { className: "text-lg" }),
        React.createElement("div", { className: "font-medium" }, title)
      ),
      React.createElement(
        "p",
        { className: "mt-2 text-sm text-neutral-600" },
        desc
      )
    )
  );
}

function ExampleCard({ title, repo, items }) {
  return React.createElement(
    Card,
    null,
    React.createElement(
      CardContent,
      null,
      React.createElement(
        "div",
        { className: "flex items-center justify-between gap-4" },
        React.createElement("div", { className: "text-lg font-medium" }, title),
        React.createElement(
          "a",
          {
            href: repo,
            target: "_blank",
            rel: "noreferrer",
            className:
              "text-sm text-blue-600 hover:underline inline-flex items-center gap-1",
          },
          React.createElement(Github, { className: "text-base" }),
          "View repo"
        )
      ),
      React.createElement(
        "ul",
        { className: "mt-3 list-inside list-disc text-sm text-neutral-700" },
        items.map((item, index) =>
          React.createElement("li", { key: index }, item)
        )
      )
    )
  );
}

function HomePage() {
  const [repoUrl, setRepoUrl] = useState("");
  const [status, setStatus] = useState({ type: "idle" });
  const [result, setResult] = useState(null);

  const isValidGithubUrl = (url) => {
    const re = /^https?:\/\/(www\.)?github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+(\.git)?(\/)?$/;
    return re.test(url.trim());
  };

  const handleGenerate = async () => {
    setResult(null);
    if (!isValidGithubUrl(repoUrl)) {
      setStatus({
        type: "error",
        message:
          "Enter a valid GitHub repository URL (e.g., https://github.com/owner/repo).",
      });
      return;
    }
    setStatus({
      type: "loading",
      message: "Scanning repository and generating MCP server…",
    });

    try {
      await new Promise((resolve) => setTimeout(resolve, 1200));
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
      setStatus({
        type: "success",
        message: "MCP server generated successfully!",
      });
    } catch (error) {
      setStatus({
        type: "error",
        message: "Something went wrong while generating the MCP server.",
      });
    }
  };

  return React.createElement(
    "div",
    { className: "min-h-screen bg-white text-neutral-900" },
    React.createElement(
      "header",
      { className: "sticky top-0 z-40 w-full border-b bg-white/80 backdrop-blur" },
      React.createElement(
        "div",
        { className: "mx-auto flex max-w-6xl items-center justify-between px-4 py-3" },
        React.createElement(
          "div",
          { className: "flex items-center gap-2" },
          React.createElement(Sparkles, { className: "text-lg" }),
          React.createElement("span", { className: "font-semibold" }, "MCP Auto-Gen")
        ),
        React.createElement(
          "nav",
          { className: "hidden gap-6 text-sm md:flex" },
          ["How it works", "Features", "Examples", "FAQ"].map((label) =>
            React.createElement(
              "a",
              {
                key: label,
                href: `#${label.toLowerCase().split(" ").join("")}`,
                className: "opacity-70 hover:opacity-100",
              },
              label
            )
          )
        ),
        React.createElement(
          "div",
          { className: "flex items-center gap-2" },
          React.createElement(
            "a",
            {
              href: "https://github.com",
              target: "_blank",
              rel: "noreferrer",
              className: "hidden md:block",
            },
            React.createElement(
              Button,
              { variant: "outline", className: "gap-2" },
              React.createElement(Github, { className: "text-base" }),
              "Star on GitHub"
            )
          ),
          React.createElement(
            Button,
            {
              className: "gap-2",
              onClick: () => {
                const el = document.getElementById("repo-input");
                if (el) {
                  el.scrollIntoView({ behavior: "smooth", block: "center" });
                  if (el instanceof HTMLInputElement) {
                    el.focus();
                  }
                }
              },
            },
            "Try it"
          )
        )
      )
    ),
    React.createElement(
      "section",
      { className: "mx-auto max-w-6xl px-4 pt-16 pb-10", id: "howitworks" },
      React.createElement(
        MotionDiv,
        {
          initial: { opacity: 0, y: 10 },
          animate: { opacity: 1, y: 0 },
          transition: { duration: 0.5 },
        },
        React.createElement(
          "h1",
          { className: "text-balance text-4xl font-bold tracking-tight md:text-6xl" },
          "Turn any GitHub repo into an ",
          React.createElement(
            "span",
            {
              className:
                "bg-gradient-to-r from-black to-neutral-500 bg-clip-text text-transparent",
            },
            "MCP server"
          ),
          " — instantly."
        ),
        React.createElement(
          "p",
          { className: "mt-4 max-w-2xl text-lg text-neutral-600" },
          "Paste a repository URL. We scan it, infer useful tools, and generate a ready-to-use MCP endpoint for your agents."
        )
      ),
      React.createElement(
        MotionDiv,
        {
          initial: { opacity: 0, y: 8 },
          animate: { opacity: 1, y: 0 },
          transition: { duration: 0.4, delay: 0.2 },
          className: "mt-8",
        },
        React.createElement(
          "div",
          {
            className:
              "mx-auto flex max-w-3xl items-center gap-2 rounded-2xl border p-2 shadow-sm",
          },
          React.createElement(LinkIcon, { className: "ml-1 text-lg opacity-60" }),
          React.createElement("input", {
            id: "repo-input",
            value: repoUrl,
            onChange: (event) => setRepoUrl(event.target.value),
            placeholder: "https://github.com/owner/repo",
            className:
              "w-full rounded-xl bg-transparent px-3 py-3 outline-none placeholder:text-neutral-400",
          }),
          React.createElement(
            Button,
            { className: "rounded-xl px-4", onClick: handleGenerate },
            "Generate MCP ",
            React.createElement(ArrowRight, { className: "text-sm" })
          )
        ),
        React.createElement(
          "div",
          { className: "mx-auto mt-3 max-w-3xl min-h-6 text-sm" },
          status.type === "error" &&
            React.createElement(
              "div",
              { className: "text-red-600" },
              status.message
            ),
          status.type === "loading" &&
            React.createElement(
              "div",
              { className: "animate-pulse text-neutral-600" },
              status.message
            ),
          status.type === "success" &&
            React.createElement(
              "div",
              { className: "text-emerald-600" },
              status.message
            )
        )
      ),
      result &&
        React.createElement(
          MotionDiv,
          {
            initial: { opacity: 0, y: 8 },
            animate: { opacity: 1, y: 0 },
            transition: { duration: 0.4, delay: 0.1 },
            className: "mx-auto mt-6 max-w-3xl",
          },
          React.createElement(
            Card,
            { className: "border-neutral-200" },
            React.createElement(
              CardContent,
              null,
              React.createElement(
                "div",
                { className: "flex items-center justify-between gap-4" },
                React.createElement(
                  "div",
                  null,
                  React.createElement(
                    "div",
                    {
                      className:
                        "text-sm uppercase tracking-wide text-neutral-500",
                    },
                    "Deployed Endpoint"
                  ),
                  React.createElement(
                    "a",
                    {
                      href: result.endpoint,
                      className:
                        "text-balance break-all text-base font-medium text-blue-600 hover:underline",
                      target: "_blank",
                      rel: "noreferrer",
                    },
                    result.endpoint
                  )
                ),
                React.createElement(
                  "span",
                  {
                    className:
                      "rounded-full bg-emerald-50 px-3 py-1 text-sm font-medium text-emerald-700",
                  },
                  `ID: ${result.serverId}`
                )
              ),
              React.createElement(
                "div",
                { className: "mt-4 rounded-xl bg-neutral-50 p-4" },
                React.createElement(
                  "div",
                  {
                    className:
                      "mb-2 flex items-center gap-2 text-sm font-medium text-neutral-600",
                  },
                  React.createElement(TerminalSquare, { className: "text-base" }),
                  "Build Logs"
                ),
                React.createElement(
                  "pre",
                  {
                    className:
                      "max-h-48 overflow-auto whitespace-pre-wrap text-sm text-neutral-800",
                  },
                  result.logs.map((line) => `• ${line}`).join("\n")
                )
              ),
              React.createElement(
                "div",
                { className: "mt-4 text-sm text-neutral-600" },
                "Use this endpoint in your agent’s MCP client to discover tools and call them securely."
              )
            )
          )
        )
    ),
    React.createElement(
      "section",
      { id: "how", className: "mx-auto max-w-6xl px-4 py-14" },
      React.createElement(
        "div",
        { className: "grid gap-6 md:grid-cols-3" },
        React.createElement(
          Step,
          { icon: React.createElement(LinkIcon, { className: "text-base" }), title: "Paste repo" },
          "Point us to your GitHub project. We handle cloning and static analysis."
        ),
        React.createElement(
          Step,
          { icon: React.createElement(Rocket, { className: "text-base" }), title: "Generate tools" },
          "We infer useful functions, endpoints, and CLI commands to expose via MCP."
        ),
        React.createElement(
          Step,
          { icon: React.createElement(ShieldCheck, { className: "text-base" }), title: "Deploy & secure" },
          "Get a versioned MCP server with auth, logs, and guardrails."
        )
      )
    ),
    React.createElement(
      "section",
      { id: "features", className: "mx-auto max-w-6xl px-4 pb-14" },
      React.createElement(
        "div",
        { className: "grid gap-6 md:grid-cols-3" },
        React.createElement(
          Feature,
          { title: "Consistent schema", desc: "All tools expose the same MCP contract, so agents can discover & call them reliably." }
        ),
        React.createElement(
          Feature,
          { title: "Language-agnostic", desc: "Python, Node, CLIs, microservices—wrap almost anything with no bespoke glue." }
        ),
        React.createElement(
          Feature,
          { title: "Zero-touch updates", desc: "When your repo changes, your MCP server updates with versioning and rollback." }
        )
      )
    ),
    React.createElement(
      "section",
      { id: "examples", className: "mx-auto max-w-6xl px-4 pb-16" },
      React.createElement(
        "h2",
        { className: "text-2xl font-semibold" },
        "Examples"
      ),
      React.createElement(
        "div",
        { className: "mt-6 grid gap-6 md:grid-cols-2" },
        React.createElement(ExampleCard, {
          title: "Weather API",
          repo: "https://github.com/owner/weather",
          items: ["GET /weather{city}", "tool: getCurrentWeather", "tool: forecast"],
        }),
        React.createElement(ExampleCard, {
          title: "Slack Bot",
          repo: "https://github.com/owner/slack-bot",
          items: ["tool: postMessage", "tool: createChannel", "tool: listUsers"],
        })
      )
    ),
    React.createElement(
      "section",
      { id: "faq", className: "mx-auto max-w-6xl px-4 pb-24" },
      React.createElement(
        "h2",
        { className: "text-2xl font-semibold" },
        "FAQ"
      ),
      React.createElement(
        "div",
        { className: "mt-6 space-y-4 text-neutral-700" },
        [
          {
            q: "Do I need a chat box to use this?",
            a: "No. Paste a repo URL and click Generate. That’s it.",
          },
          {
            q: "What does the backend need?",
            a: "An endpoint that accepts a GitHub URL, runs your Code2MCP pipeline, and returns a deployed endpoint + logs.",
          },
          {
            q: "Is this secure for private repos?",
            a: "Use GitHub App/OAuth with least-privilege scopes; deploy servers inside your VPC and enable audit logs & RBAC.",
          },
        ].map((item, index) =>
          React.createElement(
            "div",
            { key: index },
            React.createElement(
              "div",
              { className: "font-medium" },
              item.q
            ),
            React.createElement(
              "p",
              { className: "text-sm text-neutral-600" },
              item.a
            )
          )
        )
      )
    ),
    React.createElement(
      "footer",
      { className: "border-t py-10" },
      React.createElement(
        "div",
        { className: "mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 px-4 md:flex-row" },
        React.createElement(
          "div",
          { className: "text-sm text-neutral-600" },
          `© ${new Date().getFullYear()} MCP Auto-Gen. All rights reserved.`
        ),
        React.createElement(
          "div",
          { className: "flex items-center gap-4 text-sm" },
          ["Docs", "Privacy", "Terms"].map((label) =>
            React.createElement(
              "a",
              {
                key: label,
                className: "opacity-70 hover:opacity-100",
                href: "#",
              },
              label
            )
          )
        )
      )
    )
  );
}

const rootElement = document.getElementById("root");
if (rootElement) {
  ReactDOM.render(React.createElement(HomePage), rootElement);
} else {
  console.error("Root element not found; React application cannot mount.");
}

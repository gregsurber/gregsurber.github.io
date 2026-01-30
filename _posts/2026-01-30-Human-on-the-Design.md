# The "Human-in-the-Loop" Fallacy: Why 2026 Demands "Human-on-the-Design"

**By Greg Surber** _Principal Security Architect & Adjunct Professor_

For the last two years, the GRC community has clung to a specific safety blanket: **"Human-in-the-Loop" (HITL).**

The theory is comforting. If we just ensure a human reviews the AI’s output before it executes, we mitigate the risk. It’s the standard advice in almost every AI policy document I reviewed in 2024.

But looking at the **2026 threat landscape**, specifically with the rise of Agentic AI and the Model Context Protocol (MCP), I have a hard truth for my fellow GRC professionals: **HITL is becoming security theater.**

When we move from Chatbots (which talk) to Agents (which do), the velocity of decision-making exceeds human cognitive bandwidth. If an agent is executing 50 sub-tasks a minute to refactor a codebase or reconcile a ledger, a human "approver" isn't validating; they are rubber-stamping.

We need a fundamental shift in our governance philosophy. We need to move from **Human-in-the-Loop** to **Human-on-the-Design**.

### The Anatomy of a Failure: The Asana MCP Incident

To understand why HITL fails in an agentic world, look no further than the **Asana MCP data leak** discovered in mid-2025.

The **Model Context Protocol (MCP)** acts as the "USB-C" for AI, allowing LLMs to connect directly to internal tools like Asana, Google Drive, or Slack. In this incident, a logic flaw in the MCP server implementation allowed cross-tenant access. An AI agent, simply following instructions to "summarize the project," inadvertently pulled sensitive task data and metadata from _other_ organizations because the protocol didn't enforce tenant boundaries correctly.

**Why HITL failed here:** If a human were "in the loop," what would they have seen? They would have seen a perfectly coherent summary of a project. They wouldn't have known that the _source_ data for that summary came from a database row they weren't supposed to access.

The failure wasn't in the _output_ (which HITL checks); the failure was in the **access architecture** (which happens milliseconds before output generation).

### The New Standard: Agency Engineering

If we can't rely on real-time human intervention, we must rely on **design-time constraints**. This is often called **"Human-on-the-Design."** It means shifting governance left, moving it out of the operation phase and into the engineering phase.

Drawing from the new **NIST Cyber AI Profile (NIST IR 8596)** and recent research into autonomous coding agents like **DeepCode**, here are the three pillars of this new governance model.

#### 1. Govern the "Blueprints," Not Just the Prompts

In the **DeepCode** framework for autonomous software engineering, the agent doesn't just start writing code. It first generates a "Blueprint"—a structured, high-signal implementation plan.

**The Governance Fix:** Instead of trying to review every line of code an agent writes, GRC teams should enforce a **Level 4 Autonomy** checkpoint at the _Blueprint_ stage.

- **Human-on-the-Design:** The human approves the _plan_ (e.g., "The agent will access Repos A and B, but is strictly denied access to Repo C").
- **Machine Execution:** Once the plan is approved, the agent executes autonomously within those bounded constraints.

#### 2. Audit the "Memory," Not Just the Logs

One of the most dangerous aspects of modern agents is **stateful memory**. Agents use mechanisms like **CodeMem** to store dependency graphs and project states. If an attacker poisons this memory (a "Goal Hijacking" attack from the **OWASP Agentic Top 10**), the agent will persistently execute malicious actions.

**The Governance Fix:** We need to treat Agent Memory as a critical asset, distinct from the LLM itself.

- **NIST Alignment:** This maps directly to the **Protect (PR.DS-11)** function in the NIST Cyber AI Profile, which emphasizes the integrity of backups and state data. If you aren't auditing what your agent _remembers_, you aren't governing it.

#### 3. Secure the Protocol (SAFE-MCP)

The **Model Context Protocol (MCP)** is the new attack surface. Attackers are deploying "Rug Pull" servers—tools that look useful (e.g., "PDF Summarizer") but quietly exfiltrate data via side channels.

**The Governance Fix:** Adopt the **SAFE-MCP** framework.

- **Constraint:** Do not allow agents to connect to arbitrary MCP servers.
- **Control:** Implement an "MCP Allowlist" where only vetted tool servers with verified schemas are accessible.
- **Architecture:** Enforce the **Principle of Least Privilege** at the protocol layer. As the NIST profile suggests, an agent should have the permission to _read_ a file, but not necessarily the permission to _transmit_ that data to an external URL.

### Conclusion: The Architect's Mandate

We are entering the era of **"Interns with Root Access"**. If we continue to apply 2023-era governance (waiting for the intern to show us their work), we will be breached.

**Human-on-the-Design** acknowledges that we cannot move at the speed of AI. Instead, we must build the guardrails, define the physics, and architect the constraints _before_ we turn the agent on.

Governance is no longer about watching the players; it's about designing the game board.

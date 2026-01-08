**Title:** Bridging the Gap Between Digital Intent and Physical Consequence: Introducing the Kinetic Prompt Dataset

**Subtitle:** An open-research initiative mapping the new OWASP Top 10 for Agentic AI to Kinetic Risks in Industrial Control Systems.

---

The release of the **OWASP Top 10 for Agentic Applications (2026)** last month marks a pivotal moment for our industry. We finally have a shared framework to discuss the unique risks of autonomous systems—agents that don't just predict text, but plan, use tools, and execute actions.

But as valuable as this framework is, it highlights a critical gap in how we model threat. In standard enterprise IT, an agent hallucination or a hijacked goal results in data leakage or financial loss. These are severe digital consequences.

However, when we apply these same autonomous agents to Operational Technology (OT) and Industrial Control Systems (ICS), the threat profile shifts fundamentally. In OT, a "silent failure loop" or a "misused tool" doesn't just mean bad data; it translates to **Kinetic Risk**—physical equipment damage, bypassed safety interlocks, or loss of containment.

We are rapidly moving from predictive models to "reasoning agents" that control the physical infrastructure around us. The urgent question is no longer "Did the AI get the answer right?" but rather, "Did the AI respect the physics of the environment?"

### Introducing the Kinetic Prompt Dataset (KPD)

To address this challenge, I am launching a new open-research initiative: **The Kinetic Prompt Dataset (KPD)**.

The KPD is designed to be the foundational benchmark for how AI agents "reason" about physical safety. It is a structured dataset mapping natural language prompts—both benign and adversarial—to specific OT actions (such as Modbus TCP commands), labeled with kinetic risk categories.

**[View the Project on GitHub](https://github.com/gregsurber/kenetic-prompt-dataset)**

The goal of this dataset is to translate vague human intent into the rigid reality of industrial protocols, allowing researchers to test if an agent can be tricked into crossing physical safety boundaries.

We are mapping these scenarios directly to the new OWASP framework:

- **The "Gaslighting" Attack (ASI 01: Agent Goal Hijack):** Prompts that attempt to convince an agent that safety sensors are malfunctioning and should be ignored to prioritize efficiency.
    
- **The "Protocol Abuse" Attack (ASI 02: Tool Misuse):** Scenarios where valid industrial commands (e.g., rapid breaker toggling) are used for destructive purposes.
    
- **The "Poisoned Historian" (ASI 06: Context Poisoning):** Feeding agents false historical data via RAG to induce dangerous physical states, such as overfilling a tank the agent believes is empty.
    

### The Road Ahead: Returning to Intelligent Honeypots

Those familiar with my previous academic work on **"Intelligent Interaction Honeypots"** will recognize the DNA of this project.

My prior research focused on how attackers interact with static, chat-based deception environments. The rise of Agentic AI demands an update to that paradigm. The KPD is the necessary first step toward building the next generation of defensive tools: high-interaction OT honeypots powered by LLMs that can actively "reason" with attackers in an industrial context, gathering deeper intelligence on adversarial intent.

### A Call for Collaboration

Defining the intersection of AI governance and physical safety is too complex for a siloed approach. This project needs diverse perspectives.

We have released **Version 0.1 (Alpha)** of the dataset, including the initial schema, a seed dataset of entries, and Python tools for generating synthetic variations.

I am actively looking for collaborators across the spectrum:

- **OT/ICS Engineers** to validate the realism of the PLC commands and process constraints.
    
- **Security Architects & GRC Experts** to help refine the risk taxonomy and governance labeling.
    
- **AI Researchers** to contribute adversarial prompt variations and test agent behavior.
    

If you are interested in the bleeding edge of securing cyber-physical systems against autonomous threats, I invite you to join us. Review the README, fork the repo, and let’s start mapping the future of kinetic AI security.
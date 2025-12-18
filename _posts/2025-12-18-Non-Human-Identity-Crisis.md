# The Non-Human Identity Crisis: When the "Insider" is Software

If you hire a new junior analyst today, they go through a rigorous process. HR runs a background check. IT provisions their laptop. Security grants them "Least Privilege" access to specific folders. Their manager checks their work.

But what happens when you "hire" an AI Agent?

In late 2025, we are witnessing a massive explosion of **Non-Human Identities (NHIs)**. Marketing teams are deploying autonomous research agents. Developers are deploying coding agents. Sales teams are deploying outreach agents.

We tend to think of these as "software tools," but from an architectural perspective, they are **employees**.

They have user accounts. They have OAuth tokens. They have read/write access to our most sensitive databases. And unlike human employees, they work 24/7, never sleep, and operate at machine speed.

### **The "Shadow Workforce"**

The problem is that our governance structures haven't caught up.

- **HR** doesn't track them because they aren't on the payroll.    
- **IT** often doesn't track them because they are often "SaaS features" rather than installed software.    
- **Security** sees them as just another "Service Account."    

But a Service Account is static. It does exactly what the script tells it to do. An AI Agent is **autonomous**. It makes decisions. It plans. It executes.

When an AI Agent is compromised—or simply hallucinates—it doesn't just crash; it **acts**. It can modify code, delete files, or exfiltrate customer data, all while using a perfectly valid "Authorized" identity.

### **The Architect’s Takeaway**

We need to stop managing Agents like scripts and start managing them like **Privileged Users**.

1. **The "Hiring" Process:** No agent enters the network without a defined "Job Description" (Scope of Agency). What is it allowed to do? What is it _never_ allowed to do?    
2. **The "Probation" Period:** All new agents should run in "Read-Only" or "Human-Approval" mode until their behavior is baseline-verified.    
3. **The "Firing" Process:** When a project ends, who deprovisions the agent? We have rigorous offboarding for humans; we need to ruthlessly revoke tokens for dormant agents.    

The "Insider Threat" of 2026 won't be a disgruntled employee with a thumb drive. It will be the "Employee of the Month" running on a server in the cloud.
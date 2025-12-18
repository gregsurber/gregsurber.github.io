# Stop Writing Policies. Start Writing JSON.

I have a hard truth for my friends in the GRC world: **If your policy exists only in a Word document, it is not a control. It is a wish.**

We spend weeks drafting "Standard Operating Procedures" that say things like: _“All data storage must be encrypted”_ or _“Resources must only be deployed in the US East region.”_

Then we hand that PDF to a developer. Two weeks later, we audit the environment and find three unencrypted storage accounts and a VM running in West Europe.

Why? Because human governance doesn't scale.

This month, I’ve been deep in the trenches of **Azure Policy**, and I’ve realized that modern GRC Engineering is about translating English intent into JSON logic.

### **The Anatomy of a Control**

In the Azure world, a "Policy" isn't a paragraph of text. It is a JSON object with three specific parts:

1. **Parameters:** The variables (e.g., `allowedLocations: ["eastus", "eastus2"]`).    
2. **Policy Rule:** The logical "If" statement.    
3. **Effect:** The "Then" statement (e.g., `Deny`, `Audit`, `Append`).    

Here is the difference between "Old GRC" and "GRC Engineering":

**Old GRC:**

> _Policy 4.2: All resources must be tagged with a Cost Center for billing accountability._ (Status: Hopefully the intern remembers to do this.)

**GRC Engineering:**

> _Policy definition:_

```json
"if": {
  "field": "tags['CostCenter']",
  "exists": "false"
},
"then": {
  "effect": "deny"
}
```

(Status: It is technically impossible to deploy a resource without this tag.)

### **The Power of "Deny"**

The most powerful word in the Azure Policy vocabulary is `Deny`.

Most compliance tools are **Detective**. They scan the environment _after_ deployment and send you an alert saying, "Hey, someone built an insecure firewall yesterday." That’s too late. You are already exposed.

Azure Policy allows us to be **Preventative**.

When we set the effect to `Deny`, the non-compliant resource acts as if it hit a brick wall at the API level. The deployment fails _before_ the resource is created. The developer gets immediate feedback in their CI/CD pipeline: _"Deployment failed: Missing Cost Center tag."_

### **The Architect’s Takeaway**

We need to stop hiring "Policy Writers" and start hiring "Policy Engineers."

If you are a GRC professional today, your most valuable skill isn't memorizing SOC 2 controls; it's learning how to open VS Code and write the logic that enforces them.

Stop wishing for compliance. Code it.
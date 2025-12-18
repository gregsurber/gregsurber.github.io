# The End of the Screenshot Audit: Automating Evidence in Azure

There is a ritual in the GRC world that I call "Audit Week." It involves highly paid engineers sitting in a conference room, navigating to the Azure Portal, opening a firewall configuration, taking a screenshot, pasting it into a Word doc, and repeating the process 500 times.

It is tedious. It is unscalable. And frankly, it is prone to error. A screenshot is just evidence that _one_ resource was compliant at _one_ specific second in time.

If we are going to embrace **GRC Engineering**, we have to kill the screenshot.

In the Azure ecosystem, the weapon of choice for this murder is **Azure Resource Graph (ARG)**.

### **SQL for Your Infrastructure**

Most people treat the cloud portal like a GUI—clicking around to find things. But GRC Engineers treat the cloud like a database.

Azure Resource Graph allows us to query our entire infrastructure using **KQL (Kusto Query Language)**. It’s the same language used in Microsoft Sentinel, but instead of querying logs, we are querying _configuration_.

**The Old Way (The Screenshot):**
1. Click 'Virtual Machines'.    
2. Click 'My-VM-01'.    
3. Click 'Disks'.    
4. Screenshot the 'Encryption' setting.    
5. Repeat for VM-02, VM-03...    

**The GRC Engineering Way (The Query):** Instead, I write a simple query to list every disk in the entire organization that is _not_ encrypted:

Code snippet

```
Resources
| where type == "microsoft.compute/disks"
| where properties.encryption.type == "EncryptionAtRestWithPlatformKey"
| project name, resourceGroup, subscriptionId, location, properties.encryption.type
```

I can run this across 50 subscriptions instantly. The output isn't a picture; it's a dataset.

### **From "Sample" to "Population"**

Auditors usually ask for a "sample" of evidence (e.g., "Show me 10 random VMs") because they assume checking _all_ of them is impossible.

With ARG, checking all of them is actually easier than checking a sample.

We can flip the script. Instead of sending a zip file of screenshots, we can build a **Compliance Dashboard** backed by these queries. When the auditor asks, "Are your storage accounts public?", we don't say "Let me check." We point to the dashboard that says: **"0 Public Storage Accounts. Last scanned: 10 seconds ago."**

### **The Architect’s Takeaway**

Data is better than pictures.

If your evidence collection requires a human to press "Print Screen," you aren't doing Engineering; you're doing Art Appreciation.

By moving to query-based evidence, we move from "Point-in-Time" compliance (I was secure on Tuesday) to "Continuous" compliance (I am secure _right now_).
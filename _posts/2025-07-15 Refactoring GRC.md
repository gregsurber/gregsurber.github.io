# Refactoring GRC: Why I’m Porting "GRC Engineering" to Azure

I recently finished reading _GRC Engineering_ by AJ Yawn. If you work in compliance or cloud security and haven't read it, put it on your short list.

The central thesis hit me like a ton of bricks: **Governance is not a documentation problem; it is an engineering problem.**

For decades, we have treated GRC (Governance, Risk, and Compliance) as the "Department of No" or the "Department of PDF Generation." We wrote policies in Word documents, stored them in SharePoint, and then spent three weeks a year frantically taking screenshots to prove to an auditor that we were actually doing what the document said.

AJ argues for a different approach: **Continuous Compliance.** Instead of asking an admin to _promise_ they enabled encryption, we write code that _enforces_ encryption.

There is just one catch for me: The book is heavily focused on the AWS ecosystem (AWS Config, CloudTrail, etc.).

But my daily reality—and the reality for many enterprise architects—is **Microsoft Azure**.

### **The "Rosetta Stone" of Cloud Governance**

So, I am embarking on a project. Over the next few months, I am going to take the principles of GRC Engineering and port them, line by line, into the Azure stack.

The philosophy remains the same, but the tooling needs a translation layer:

1. **The Rule Engine:**    
    - _AWS:_ AWS Config Rules        
    - _Azure Translation:_ **Azure Policy**. This is the heart of the system. We aren't just "monitoring"; we are using `Deny` effects to stop non-compliant resources from ever being born.
        
2. **The Evidence Collector:**    
    - _AWS:_ AWS CLI / Boto3 scripts        
    - _Azure Translation:_ **Azure Resource Graph (ARG)**. This is a superpower that doesn't get enough love. It allows us to query our entire infrastructure using KQL (Kusto Query Language) to generate real-time audit evidence in milliseconds.
        
3. **The Remediation Layer:**    
    - _AWS:_ Lambda functions        
    - _Azure Translation:_ **Azure Event Grid + Logic Apps**. Moving from "polled" compliance to "event-driven" compliance.        

### **Why "Policy as Code" Matters**

As an Architect, I prioritize **determinism**. I need to know that if I deploy a subscription in East US, it will have the exact same security posture as a subscription in West Europe.

You cannot achieve determinism with a checklist. You can only achieve it with code.

If our "Governance" lives in a PDF, it is a suggestion. If our "Governance" lives in Terraform or Bicep, it is a **constraint**.

### **The Road Ahead**

This isn't just an academic exercise. I am looking to build a "Paved Road" for my developers—a way for them to move fast without breaking things.

In the coming posts, I’ll be diving deep into:
- Writing custom Azure Policy definitions to replace manual checks.    
- Killing the "Screenshot Audit" using ARG queries.    
- Automating remediation so I can sleep at night.    

We are moving GRC out of the spreadsheet and into the IDE. Let’s get to work.
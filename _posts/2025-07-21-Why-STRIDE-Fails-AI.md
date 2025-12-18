# Threat Modeling for Stochastic Systems: Why STRIDE Fails AI

I spent three hours yesterday in a threat modeling session for a new GenAI customer support bot. We had the whiteboard out. We had our trusty architecture diagrams. And we had **STRIDE**.

For the uninitiated, STRIDE is the bread and butter of application security. It stands for **S**poofing, **T**ampering, **R**epudiation, **I**nformation Disclosure, **D**enial of Service, and **E**levation of Privilege. It has served us well for 20 years.

But about 45 minutes in, I realized we were trying to force a square peg into a round hole.

When an engineer asked, _"What if the user convinces the bot to offer a discount we didn't approve?"_, the room went quiet.

Was that **Tampering**? No, the code wasn't changed. Was it **Elevation of Privilege**? Sort of, but the user identity didn't change. Was it **Information Disclosure**? Not really.

We were stuck because STRIDE is built for **Deterministic Systems**. In traditional software, `Input A` + `Function B` always equals `Output C`. If it doesn't, it's a bug or an exploit.

AI systems are **Stochastic** (probabilistic). `Input A` might equal `Output C` today, but `Output D` tomorrow.

### **The "Probability" Gap**

The fundamental issue is that AI introduces failure modes that are **cognitive**, not just technical.

1. **Prompt Injection vs. Input Validation:** In a SQL Injection attack (caught by STRIDE's "Tampering"), we can sanitize the input because we know exactly what "bad" looks like (e.g., `1=1`). In Prompt Injection, the input ("Ignore previous instructions") is valid English. It’s not "malicious code"; it’s "malicious persuasion."    
2. **Hallucination vs. Data Integrity:** If a database returns the wrong record, that's an integrity failure. If an LLM invents a court case that never happened, the system is working _exactly as designed_ (predicting the next likely token). STRIDE has no bucket for "The system worked perfectly, but the output is a lie."    

### **Moving from STRIDE to ATLAS**

If you are an Architect trying to secure LLMs this year, you need a new dictionary. I’ve stopped using STRIDE for the model layer and started using **MITRE ATLAS** (Adversarial Threat Landscape for Artificial-Intelligence Systems).

ATLAS gives us the vocabulary we were missing in that conference room:
- **LLM Jailbreak** (instead of just Privilege Escalation)    
- **Model Evasion** (instead of just Tampering)    
- **Inversion Attacks** (instead of just Info Disclosure)    

### **The Architect’s Takeaway**

We don't need to throw out STRIDE entirely—it’s still vital for the API wrapper, the database, and the cloud infrastructure hosting the model.

But for the model itself? Stop trying to treat it like a database. You cannot "firewall" a probability. You have to govern it.

If you’re still using a 2010 threat model for a 2025 AI agent, you aren't finding risks. You’re just documenting your own blind spots.

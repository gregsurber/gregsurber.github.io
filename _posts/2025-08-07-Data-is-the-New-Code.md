#  Data is the New Code: The Rise of the "Data Supply Chain"

If you walked into a Security Operations Center (SOC) five years ago and asked about the "supply chain," everyone would immediately talk about **SolarWinds** or **Log4j**. We spent half a decade building rigorous pipelines to scan every line of code, every library, and every dependency. We now have SBOMs (Software Bill of Materials) for everything.

But here is the uncomfortable truth I’m seeing in 2025: **We are securing the wrapper and ignoring the candy.**

A modern AI system is maybe 20% Python code and 80% Training Data.

We are applying world-class DevSecOps to the 20% (the code) while leaving the 80% (the data) completely unmonitored. We scrape it, we buy it, we ingest it, and we trust it.

### **Garbage In, Liability Out**

In the old days of data science, we had a saying: "Garbage In, Garbage Out." It meant if your data was bad, your model was inaccurate.

In the age of GenAI, that saying has changed. It is now: **"Poison In, Breach Out."**

If an attacker poisons a subset of your training data—inserting a "trigger phrase" that causes the model to bypass safety rails—no amount of SAST/DAST scanning on the Python code will catch it. The vulnerability isn't in the syntax; it's in the _weights_ of the model itself.

And it’s not just security; it’s legal risk. If your model was trained on data you don't have the rights to use, you haven't built a proprietary asset. You’ve built a copyright lawsuit waiting to happen.

### **The Missing Control: Data Provenance**

As Architects, we need to stop treating datasets like static files and start treating them like **software dependencies**.

We need a **Data BOM (Bill of Materials)**.

Before any dataset enters your training or fine-tuning pipeline, you need to answer three questions:
1. **Provenance:** Where specifically did this come from? (Not just "the internet," but which domain, which scrape date?)    
2. **Integrity:** Has it been modified since ingestion? (Hash verification for data shards).    
3. **License:** Do we actually have the right to use this for commercial inference?    

### **The Architect’s Takeaway**

It is time to extend the "Shift Left" mentality to data engineering.

If you cannot trace a specific output token back to the specific document that influenced it, you don't have a secure system. You have a stochastic parrot with a mystery supply chain.

Stop scanning the container and start scanning the contents.
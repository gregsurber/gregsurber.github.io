---
layout: single
title: "ICS-SimLab: A Containerized Approach for Simulating Industrial Control Systems for Cyber Security Research"
date: 2026-01-10
categories: news             # <--- This puts it on the News page
link_url: "https://arxiv.org/abs/2509.23305"  # <--- The "Original Source" link
---

The cat-and-mouse game of IoT security just got a major upgrade.

For years, security researchers have faced a dilemma: Low-interaction honeypots are cheap but easily spotted by sophisticated attackers. Physical testbeds are realistic but prohibitively expensive and hard to scale.

Enter ICS-SimLab, a proposed framework that uses Docker containerization to simulate Industrial Control Systems (ICS) with startling accuracy. By replicating the Purdue Enterprise Reference Architecture entirely in software, ICS-SimLab might just be the "missing link" we need to build honeypots that are both scalable and unspotable.

Here is why this research is a potential game-changer for IoT threat hunting:

1. Faking Physics, Not Just Packets
Most honeypots fail because they are static—they don't "react" like a real machine. ICS-SimLab changes this by using Hardware-in-the-Loop (HIL) modules to simulate physical physics. If an attacker sends a command to open a valve, the system simulates the water level changing. This dynamic feedback loop makes it exponentially harder for adversaries to distinguish the simulation from a real water treatment facility.

2. Infinite Scale, Zero Hardware
Projects like SIPHON proved that distributed "wormholes" are effective, but they still rely on a backend of physical devices. ICS-SimLab replaces that expensive hardware with lightweight Docker containers.

Need a gas pipeline? Load a JSON config.

Need a smart grid? Spin up a new container stack. Researchers can now present a diverse, shifting attack surface to the internet without buying a single PLC.

3. Fuel for "Intelligent" Defense
We know that the future of honeypots is AI (as seen in projects like IoTCandyJar), but training those models requires massive amounts of behavioral data. ICS-SimLab is effectively a "data factory," capable of running automated attack scenarios to generate the clean, labeled datasets needed to teach intelligent agents how to mimic real-world devices.

4. A Safe Space for Malware Forensics
Modern IoT botnets are nasty—they kill competing processes and fight for persistence. Because ICS-SimLab isolates the control logic in containers, it offers a perfect "sandbox" to observe these anti-forensics techniques safely. Researchers can watch exactly how malware attempts to modify PLC logic or disrupt HMI communications without risking operational infrastructure.

5. The Ultimate "Turing Test" for Honeypots
Before a honeypot goes live, it needs to be vetted. ICS-SimLab allows researchers to run "pre-flight checks" against known fingerprinting tools (like Shodan’s Honeyscore). If the simulation can fool the scanner in the lab, it stands a much better chance of fooling the attacker in the wild.

The Bottom Line: ICS-SimLab represents a shift from "security through obscurity" to "security through high-fidelity simulation." By combining the flexibility of Docker with the realism of physics simulations, we are moving closer to a world where attackers can never be quite sure if they have breached a critical system—or just walked into a very sophisticated trap.

Stay tuned for our full deep-dive analysis on how we are integrating ICS-SimLab into our kinetic risk investigations.
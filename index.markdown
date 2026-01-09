---
layout: splash
permalink: /
title: "Principal Security Architect & GRC Executive"
header:
  overlay_color: "#333"
  caption: "Strategic GRC • AI Governance • Critical Infrastructure"
---

I am a Senior Cybersecurity Executive and GRC Strategist with over 20 years of experience securing regulated environments (DoD, Energy, Biotech). My focus is two-fold: Building defensible, FedRAMP-ready security programs today, and defining the governance standards for Kinetic AI Risk tomorrow.

## Latest Thoughts

{% for post in site.posts limit:3 %}
* [**{{ post.title }}**]({{ post.url }}) - *{{ post.date | date_to_string }}* <br> {{ post.excerpt | strip_html | truncatewords: 30 }}
{% endfor %}

---
layout: splash
permalink: /
header:
  overlay_color: "#333"
  caption: "Security Architecture • AI Governance • Risk Management"
excerpt: >
  I am a Principal Cybersecurity Architect with 20+ years of experience engineering GRC solutions. 
  I am currently researching the next frontier: **Kinetic AI Risk**—governing the intersection 
  of Agentic AI and Critical Infrastructure.
---

## Latest Thoughts
{% for post in site.posts limit:3 %}
* [**{{ post.title }}**]({{ post.url }}) - *{{ post.date | date_to_string }}* <br> {{ post.excerpt | strip_html | truncatewords: 30 }}
{% endfor %}

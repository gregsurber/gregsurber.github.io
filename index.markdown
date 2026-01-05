---
layout: splash
permalink: /
header:
  overlay_color: "#333" # or use overlay_image: /assets/images/banner.jpg
  caption: "Security Architecture • AI Governance • Risk Management"
excerpt: >
  I am a Principal Cybersecurity Architect with 20+ years of experience securing infrastructure 
  and engineering GRC solutions. I am currently pivoting to the next frontier: **AI Governance**.
  
  <br /> <a href="/resume/" class="btn btn--light-outline btn--large">View My Resume</a>
---

## Latest Thoughts
{% for post in site.posts limit:3 %}
* [**{{ post.title }}**]({{ post.url }}) - *{{ post.date | date_to_string }}* <br> {{ post.excerpt | strip_html | truncatewords: 30 }}
{% endfor %}
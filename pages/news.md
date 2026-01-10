---
layout: archive
title: "Curated News & Reading List"
permalink: /news/
---

Here I collect important articles regarding AI Risk, NIST frameworks, and Cybersecurity trends, along with my brief analysis.

{% assign news_posts = site.categories.news %}
{% for post in news_posts %}
  <article class="archive__item">
    <h3 class="archive__item-title"><a href="{{ post.url }}">{{ post.title }}</a></h3>
    <p class="archive__item-excerpt">{{ post.content | markdownify | strip_html | truncatewords: 50 }}</p>
    <p><small><i class="fas fa-link"></i> <a href="{{ post.link_url }}">Original Source</a></small></p>
  </article>
{% endfor %}
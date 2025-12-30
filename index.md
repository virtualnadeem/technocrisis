---
layout: default
title: Feed
---

# TechnoCrisis
Real time analysis of systems breaking at scale
## Latest signals

<ul class="post-list">
{% for post in site.posts limit:20 %}
  <li class="post-card">
    <div class="post-meta">{{ post.date | date: "%b %d, %Y" }}</div>
    <a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    {% if post.excerpt %}
      <p class="post-excerpt">{{ post.excerpt | strip_html | truncate: 160 }}</p>
    {% endif %}
  </li>
{% endfor %}
</ul>

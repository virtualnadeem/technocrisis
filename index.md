---
layout: default
title: Writing
---

# TechnoCrisis

Critical writing on AI, automation, and technological risk.

Technology rarely fails loudly.  
It reshapes systems quietly, until those systems begin to break.

## Latest posts

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

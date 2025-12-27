---
layout: default
title: Home
---

# TechnoCrisis
Real-time analysis of technology crises.

## Latest
{% for post in site.posts limit:20 %}
- [{{ post.title }}]({{ post.url }}) — {{ post.date | date: "%b %d, %Y" }}
{% endfor %}

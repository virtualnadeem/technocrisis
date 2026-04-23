import json
import random
import datetime
import re
from pathlib import Path

ROOT = Path(__file__).parent
POSTS_DIR = ROOT / "_posts"
TOPICS_FILE = ROOT / "topics.json"

with open(TOPICS_FILE, "r", encoding="utf-8") as f:
    topics = json.load(f)

topic = random.choice(topics)
date = datetime.datetime.now().strftime("%Y-%m-%d")

slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
filename = POSTS_DIR / f"{date}-{slug}.md"

content = f"""---
layout: post
title: "{topic}: An AI Perspective on Risk"
date: {date}
---

Imagine a world where {topic.lower()} becomes normal.

## The Promise

Every powerful technology begins as a solution.

## The Hidden Risk

The danger appears when people stop questioning the system and start adapting themselves to it.

## What Could Go Wrong

When {topic.lower()} scales, society may become more efficient, but also more dependent, less human, and easier to control.

## Final Reflection

Technology rarely announces its worst consequences in advance. It arrives as convenience first, then becomes structure, then dependence.
"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Created: {filename}")

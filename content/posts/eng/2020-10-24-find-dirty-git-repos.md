---
title: Find dirty git repos
date: 2020-10-24 16:37:01
tags: [shell]
layout: post
telegram_id: 464
---

🐚 Recursively find all git repos with uncommited or unpushed changes:

```bash
find . -type d -iname '.git' -exec sh -c 'cd "${0}/../" && git status | grep -q -E "(diverged|Changes|is ahead of)" && pwd' "{}" \;
```

In case if you forgot to push something before changing a laptop (or a company).

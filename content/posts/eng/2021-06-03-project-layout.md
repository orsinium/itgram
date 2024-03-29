---
title: project-layout
date: 2021-06-03 14:25:12
tags: []
layout: post
telegram_id: 503
---

Two months ago, a hot discussion was started by a Go core developer in the "[standard go project layout](https://github.com/golang-standards/project-layout)" repository:

[this is not a standard Go project layout](https://github.com/golang-standards/project-layout/issues/117)

The short version is that some people come into Go, look for a standard project layout (how to name files and how to group them), don't find an official one, search for something, find this one, and stick to it as the "best practice". The truth is that it is highly opinionated and not in any way is the only way to go. Since then, the author of the repository slightly updated the readme with a few small disclaimers but the issue is still open and discussion is still going.

I personally found this blog post a good answer to the topic:

[Thoughts on how to structure Go code](https://changelog.com/posts/on-go-application-structure)

TL;DR: name things after the domain terms, not the framework/language ones. I suppose, the motivation to write this post was the discussion above but the idea isn't new. The first time I've heard it from Bob Martin in his "Clean Architecture": [Clean Code - Uncle Bob / Lesson 5](https://youtu.be/sn0aFEMVTpA?t=4514).

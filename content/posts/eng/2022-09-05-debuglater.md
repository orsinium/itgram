---
title: debuglater
date: 2022-09-05 16:04:01
tags: [python]
layout: post
telegram_id: 556
---

🐍 [debuglater](https://github.com/ploomber/debuglater) is a Python library that saves stacktrace into a file when your app crashes with an exception. Not just a traceback, but the whole stack, including all variables. It's all is saved using [dill](https://github.com/uqfoundation/dill), so if you have the same code, you can load the saved stacktrace into a pdb session and debug the crash, as if you could if you had put an actual breakpoint into the place of failure. Pretty cool, huh?

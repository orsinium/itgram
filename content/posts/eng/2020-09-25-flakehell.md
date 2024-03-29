---
title: flakehell
date: 2020-09-25 13:49:27
tags: []
layout: post
telegram_id: 446
---

I made an online playground for [FlakeHell](https://github.com/life4/flakehell).

Try: [flakehell.orsinium.dev](https://flakehell.orsinium.dev/)
Source: [github.com/life4/flakehell-online](https://github.com/life4/flakehell-online)

So, you can try right from browser different Python linters, like [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide), [pylint](https://github.com/PyCQA/pylint), my beloved [deal](https://github.com/life4/deal), and so on.

The fun thing is how it works. I run Python linter (and a few helper scripts) on top of [pyodide](https://github.com/iodide-project/pyodide) (it is patched [CPython](https://github.com/python/cpython) compiled into WASM), which is managed through JS-bindings from Go application compiled into [WASM](https://webassembly.org/) and using [GWeb](https://github.com/life4/gweb) library. 🤯 We need to go deeper!

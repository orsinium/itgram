---
title: SimpleParsing
date: 2022-11-09 15:58:02
tags: [python]
layout: post
telegram_id: 572
---

[SimpleParsing](https://github.com/lebrice/SimpleParsing) is a little Python library that "does one job and does it well".

If you, like me, want everything in your Python code to be type annotated (for the sake of autocomplete, semantic syntax highlighting, and safety) you may know that the container that [argparse](https://docs.python.org/3/library/argparse.html) returns (argparse.Namespace) isn't type checked because mypy can't statically know what flags and of what type you registered in ArgumentParser. And if you want to make it type-safe, there is quite a bit of boilerplate: define flags, define type safe container, unpack flags into the container. And if the definition and the container mismtch, well, your code is wrong.

SimpleParsing solves exactly this problem. You define a [dataclass](https://docs.python.org/3/library/dataclasses.html) class, annotate attribute types, set defaults, add comments to attributes, and then SimpleParsing will turn it into CLI args. Attribute names will form names of the CLI flags, types will be checked, defaults will be respected, and comments will be turned into help messages.

I've seen quite a few alternatives for that task, and all of them work on top of pydantic, click, or attrs. And I really like that SimpleParsing works with what we already have in stdlib, without bringing unnecessary dependencies.

And don't listen to anyone, [click](https://github.com/pallets/click) sucks. Testing it is quite hard, functions with 20 arguments and 20 decorators on top aren't nice, and passing all that stuff deeper into the code is hard and verbose. Using click will encourage dirty and verbose code and bad practice. Oh, and IMHO the CLI it produces is worse than that of argparse.

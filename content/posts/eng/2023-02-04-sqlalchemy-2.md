---
title: SQLAlchemy 2.0.0
date: 2023-02-04 15:29:01
tags: [python]
layout: post
telegram_id: 581
---

A week ago, [SQLAlchemy 2.0.0 was released](https://www.sqlalchemy.org/blog/2023/01/26/sqlalchemy-2.0.0-released/). Now, the default way to describe ORM models is using declarative type-annotations based definitions. So, the fields instead of `id = Column(Integer)` can be described as just `id: int`. In some cases, it can get more verbose, but it pays back by better IDE integration, syntax highlighting, type checking, and other cool stuff that comes with type annotations.

I wanted to try different alternative ORMs with asyncio and typing support, but never got to it. Now I think that it gets quite hard to beat SQLAlchemy. The project, despite being very old, still keeps up the pace (what I can't say about Django ORM, Pony ORM, or Peewee) and has very good support for modern practice. Namely, for asyncio and type annotations.

Anyway, there are some asyncio-powered ORMs that I haven't tried but that look interesting:

+ [sqlmodel](https://github.com/tiangolo/sqlmodel) is a thin wrapper on top of pydantic and sqlalchemy from the author of FastAPI. It's not actively maintained but there is not that much of code for it to be a big problem. This is the most popular ORM on this list because the author is famous.
+ [ormar](https://github.com/collerek/ormar) is another wrapper on top of pydantic and sqlalchemy to consider. Don't get deceived by the number of commits, though, they all are from dependabot.
+ [tortoise-orm](https://github.com/tortoise/tortoise-orm) is an asyncio ORM inspired by Django ORM. At this point, I'm not sure anymore that it's a good idea. A long time ago, I used to like Django ORM for its similicity, but now I'm more skeptical about this simplicity as I learned how much of poor performance and testability it costs. Internally, it uses [pypika](https://github.com/kayak/pypika) for building the queries.
+ [piccolo](https://github.com/piccolo-orm/piccolo) has quite a nice query builder but model definitions aren't declarative. Also, they say its "fully type annotated" but that's not what you might expect. There is `Any` all around, and no type safety at all in what the queries return.

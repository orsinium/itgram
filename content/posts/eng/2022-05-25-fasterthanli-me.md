---
title: "fasterthanli.me"
date: 2022-05-25 15:08:00
tags: [golang, rust]
layout: post
telegram_id: 530
---

[fasterthanli.me](https://fasterthanli.me/articles) is a relatively popular blog dedicated to comparing how better Rust is than Go. Well, it's a personal blog of a guy, so it's not dedicated to anything in particular, but feels like this is the main theme for most of the posts. Even if it's about just Rust, comparison with Go will pop up. For example:

+ [Lies we tell ourselves to keep using Golang](https://fasterthanli.me/articles/lies-we-tell-ourselves-to-keep-using-golang)
+ [Some mistakes Rust doesn't catch](https://fasterthanli.me/articles/some-mistakes-rust-doesnt-catch)
+ [I want off Mr. Golang's Wild Ride](https://fasterthanli.me/articles/i-want-off-mr-golangs-wild-ride)
+ [Aiming for correctness with types](https://fasterthanli.me/articles/aiming-for-correctness-with-types)

And you know what? Being an engineer who loves Go and avoids Rust, I agree with most of the things (if not all of them, I don't keep the score). The type system in Go sometimes is too forgiving and even the existing type system could've been used better in stdlib.

A good example (that is also covered in the blog) is having `string` as the type for filesystem paths. It prompts so many bugs, from messing the argument order to concatenating paths as they were just, well, regular strings. And all of it could've been solved just by having `type Path string` declaration. What's interesting, there is a `time.Duration` type which does exactly this. Instead of passing time in seconds (Python, C) or microseconds (Erlang, Elixir) and messing with it each time, you explicitly specify the units when building the type. For example, `5 * time.Second`. Just beautiful and much safer.

So, when you write anything on a language with a type checker (in the modern world, it's almost every language), I urge you to create subtypes for things and don't just use strings and integers. It's not so hard and it makes the code so much safer and more readable.

Oh, and I recommend reading this blog, even if you don't care about Rust or code correctness.

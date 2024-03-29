---
title: Learning Rust
date: 2022-09-16 15:18:01
tags: []
layout: post
telegram_id: 567
---

If you want to learn [Rust](https://www.rust-lang.org/), the official website provides you 3 options: [book](https://doc.rust-lang.org/book/), [course](https://github.com/rust-lang/rustlings/), and [examples](https://doc.rust-lang.org/stable/rust-by-example/). I started with the examples, and they are very bad. The first example is a classic Hello World but instead of just showing how to print text and move on, the resource goes into a lengthy explanation of what traits you need to inherit in your custom classes to make them printable. Without even explaining what is trait.  And the same trend goes through all examples: dive into some details and use a bunch of terms without explaining them or even linking. I'm still not sure who's the target audience.

So, if you want to learn Rust, read the book, the book is pretty good.

The language itself is pretty strange too. Most modern languages realized that code is for humans, and the central goal of syntax and most of the high-level features should be readability and the [principle of least surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment). And then there is Rust which consists of some obscure symbols, implicit behaviors, and strange decisions.

Rust requires each line of code to end with a semicolon. This is a strange decision for a modern language on its own. Most modern languages realized that you can tokenize code without it, and explicit semicolons are just visual noise.

But the best example of strange decisions is how to return a result from a function in Rust. In Python and Go, you always have to write an explicit return statement. In Elixir, Haskell, and Ruby function implicitly return the last expression. So, if you don't want to return anything, you make sure that the last expression is nil, which is, again, explicit.

Now, rust solves it in a very unique way. Instead of having an explicit return statement or nil at the end, it decides whether to return the expression or not based on if there is a semicolon at the end. If the line doesn't end with a semicolon, the result is returned. If it has a semicolon, a void is returned. Now, imagine you're reading some Rust code without going through the whole Rust book. What are the odds you'll figure it out? Some people will point out that the compiler will fail with a detailed error message if the semicolon and type annotation don’t match, but I’m talking about the experience of reading the code, not writing it.

At some point, people stopped using concise but hard-to-read languages, like [Perl](https://en.wikipedia.org/wiki/Perl) or [APL](https://en.wikipedia.org/wiki/APL_(programming_language)). Well, there are still there but definitely not mainstream.  Also, languages started to get rid of visual noise. You'll hardly find semicolons in most of them. I can't recall modern languages (except for PHP) that require a special symbol each time you need a variable. Many strictly typed languages, like Go, have some basic type inference.  And here we are again, Rust gets into the mainstream with compiler-centric syntax.

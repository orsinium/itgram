---
title: Testing in Rust
date: 2023-04-25 15:49:01
tags: [rust]
layout: post
telegram_id: 602
---

🦀 The built-in Rust testing framework is alright for small tests, but it quickly falls apart when the project grows. And even for small projects, the tests look messy and the failure output isn't helpful. I haven't found one all-in framework like pytest but there are some small projects that together make something much better:

+ [nextest](https://nexte.st/) is a fast test runner with a nice colorful output, powerful DSL for filtering tests to be run, and built-in mechanism for detecting slow and flaky tests. And the great thing is that it runs regular Rust tests, so you don't need to change anything in the prject itself to use it.

+ [proptest](https://github.com/proptest-rs/proptest) is a [hypothesis](https://github.com/HypothesisWorks/hypothesis)-inspired framework for writing property-based tests. You tell it what kind of input you want for your test, and it generates random values, trying to cover as many corner cases as possible. When a test fails, it finds a nice and small example for reproducing the failure.

+ [rstest](https://github.com/la10736/rstest) is a library that provides pytest-like fixtures and test parametrization (for table-driven testing). I'm not sure if fixtures is a good idea (I wrote [pytypest](https://github.com/orsinium/pytypest) for Python just to fix the mess that pytest fixtures bring in big projects) but parametrization is a must. You can also try [test-case](https://github.com/frondeus/test-case) library, it looks similar but also lets you to specify a name for each case.

+ [k9](https://github.com/aaronabramov/k9) provides a macro for snapshot testing. It dumps on disk whatever data you pass into it on the first run, and later on consequent runs compares the new value with the dumped one.

+ A better assert statement is still in question. The built-in `assert!` and `assert_eq!` do not provide a helpful enoug error message, far cry from what you can see in pytest or ex_unit. k9 and [pretty-assertions](https://github.com/rust-pretty-assertions/rust-pretty-assertions) provide some additional assertions but that's still not enough. In particular, I right away miss something like `assert_is_close` for comparing floats or an assertion that will show the arguments with which the target function was called. There is [approx](https://docs.rs/approx/latest/approx/) library just for that but I think adding a library for each assertion type doesn't scale well.

I wonder if the built-in Rust macro system allows making a nice looking assert macro with pytest-like source rewrites. Like a macro that will convert `magic_assert!(f(a, b) > x)` into `assert!(f(a, b) > x, "f({}, {}) > {}", a, b, x)`.

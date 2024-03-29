---
title: "Tail recursion"
date: 2018-08-14 12:00:01
tags: [python]
layout: post
telegram_id: 231
---

[Tail recursion](https://bit.ly/2w601IW) -- это такая рекурсия, когда вызов функцией самой себя происходит в самом конце. Такую рекурсию довольно просто разобрать на цикл, а циклы эффективнее по памяти, т.к. не требуют хранить и раскручивать весь стэк вызовов. Многие языки программирования имеют встроенную оптимизацию для такой рекурсии. Python -- нет, но написать её крайне просто.

1. [Tail Recursion In Python](https://chrispenner.ca/posts/python-tail-recursion) -- статья с простой реализацией через поднятие исключений.
2. [tco](https://github.com/baruchel/tco) -- довольно жирная реализация через исключения с кучей фич.
3. [pytailcall](https://github.com/mynameisfiber/pytailcall) -- 3 экспериментальных реализации через хакинг байткода. Немного деталей есть в [статье](https://blog.fastforwardlabs.com/2015/04/23/bytecode-hacking-for-great-justice.html). В ридми не написано, как это использовать, так что смотрите в [бенчмарк](https://github.com/mynameisfiber/pytailcall/blob/master/pytailcall/benchmark.py#L34)

Реализацию без исключений (которые, к сожалению, довольно медленные) в виде пакета я [нашёл](https://github.com/ac1235/python-tailrec/blob/master/tailrec.py), но лучше её не используйте, в ней есть некоторые проблемы.

Хвостовая рекурсия -- кейс редкий, но довольно интересный, да. Have a fun :)

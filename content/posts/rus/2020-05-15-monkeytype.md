---
title: MonkeyType
date: 2020-05-15 14:23:18
tags: []
layout: post
telegram_id: 406
---

Итак, ситуация: вам нужно аннотировать типы для тонны Python кода.

+ [MonkeyType](https://github.com/instagram/MonkeyType) — отслеживает все вызовы в рантайме, запоминает типы аргументов функций и возвращаемых значений. Instagram просто запускает какой-то небольшой процент трафика с прода на отдельный инстанс, запущенный с monkeytype, и так собирает типы.

+ [PyAnnotate](https://github.com/dropbox/pyannotate) — похожая штука от Dropbox. Поддерживает второй питон, имеет ключик `-s` чтобы применять только самые простые типы.

+ [pytest-annotate](https://github.com/kensho-technologies/pytest-annotate) — плагин для pytest, интегрирующий pyannotate.

+ [pytype](https://github.com/google/pytype) — альтернатива mypy с выведением типов от Google. Отличная штука, но глючная. Не факт, что заведётся на крупном проекте, но попробовать очень советую. Если вам повезло, и он успешно вывел типы, то получившиеся стабы можно применить обратно на код.

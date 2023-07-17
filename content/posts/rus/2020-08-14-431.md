---
title: pytest-repeat
date: 2020-08-14 17:00:10
tags: []
layout: post
telegram_id: 431
---

Полезные плагины для pytest:

- [pytest-repeat](https://github.com/pytest-dev/pytest-repeat) -- позволяет запускать один тест  много раз. Например, пока он не упадёт.
- [pytest-randomly](https://github.com/pytest-dev/pytest-randomly) -- перемешивает порядок тестов. Помогает отловить сайд-эффекты, когда один тест работает только если перед ним сработал другой (или наоборот, не работает).
- [pytest-xdist](https://github.com/pytest-dev/pytest-xdist) -- позволяет запускать тесты в несколько процессов.
- [pytest-test-groups](https://github.com/mark-adams/pytest-test-groups) -- возволяет запустить только часть процессов. Полезно на Gitlab CI для параллелизации.

Если используете pytest-test-groups вместе с pytest-randomly, то надо задать seed для последнего, чтобы тесты правильно распределились по группам. Вот пример для Gitlab CI:

```pytest:
  stage: test
  parallel: 4
  script:
    - >
      pytest -vv
      --test-group-count $CI_NODE_TOTAL
      --test-group $CI_NODE_INDEX
      --randomly-seed $CI_PIPELINE_ID```

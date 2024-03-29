---
title: cookiecutter
date: 2018-05-10 10:30:02
tags: []
layout: post
telegram_id: 138
---

[cookiecutter](https://github.com/audreyr/cookiecutter) — CLI для создания шаблонов проектов. Написан на питоне, но никак не привязан к  конкретному языку. Под капотом шаблонизация через Jinja2 и конфигурирование через JSON или YAML. Готовые шаблоны [перечислены в README](https://github.com/audreyr/cookiecutter#a-pantry-full-of-cookiecutters) и есть на все случаи жизни, в том числе куча реализаций для Django.

Хотя, я думаю, вы захотите сделать свои, что-то доработать. Хотя бы касательно вида <https://settings.py> у всех своё мнение. Мы так вообще его через [ansible vault](https://docs.ansible.com/ansible/2.4/vault.html) решили собирать. А в недавнем посте про 12 факторов (и много где ещё) рекомендуется использовать переменные окружения, поэтому рекомендую присмотреться к [decouple](https://github.com/henriquebastos/python-decouple) и  [dj-database-url](https://github.com/kennethreitz/dj-database-url). К слову, если кто-то хочет сделать хорошее для Open Source, подобных dj-something-url не хватает для кеширования и прочего.

P.S. Ну а я, по множеству причин, в простых проектах рекомендую не извращаться и ориентироваться на settings/<https://local.py> файл. Думаю, я когда-нибудь сделаю для этого ещё один cookiecutter шаблон.

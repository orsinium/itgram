---
title: "fluent-reader"
date: 2023-07-17
---

A long time ago, I used to use Twitter to find out about new projects and blog posts. Later, I moved to Reddit. Now, both are the very manifestation of [enshittification](https://en.wiktionary.org/wiki/enshittification), so I removed both accounts. [Hacker News](https://news.ycombinator.com/) never seemed useful to me (perhaps, I just don't know how to use it). I recently [registered on Mastodon](https://fosstodon.org/@orsinium) and started to follow a few hashtags, but they include a lot of unimportant stuff, like discussions, questions, and personal project updates.

So, looks like it's time to go back to RSS. [I've run a poll on Mastodon](https://fosstodon.org/@orsinium/110722419119038296) and seems like 92% of Mastodon users (740+ respondents) read RSS feeds. I'm quite surprised by the results because RSS seemed to me like something that left mainstream a long time ago, like IRC, forums, and the alike. And even if that's a bias of Mastodon users, that's still impressive.

[fluent-reader](https://github.com/yang991178/fluent-reader) is the best RSS reader I found so far. Cross-platform, nice UI, nice previews, built-in browser. I tried to find something that isn't Electron but the truth is that many websites cannot be properly rendered without a full-featured browser. Out of all feeds I tried, Mastodon caused the most trouble. You can get an RSS feed for any Mastodon account (for example, [here is mine](https://fosstodon.org/@orsinium.rss)) but there are no titles and if you follow the link, it won't render anything without JS. So, if you want to read Mastodon RSS feeds, it's important for the reader to properly render descriptions or support JS for opened links. And fluent-reader does both.

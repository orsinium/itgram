---
title: Android automation
date: 2022-02-02 16:05:28
tags: []
layout: post
telegram_id: 525
---

By accident, I dropped everything from my phone. Not in the first time, to be said. it made me think that I need 2 things:

1. "Infra as a code" for all applications.
2. rsync for photos.

Today we'll talk about the first one. In particular, about automating installation of apps on an android phone. I made for myself a few simple Python scripts that iterate over hardcoded app IDs and call the following tools:

+ bloatware can be removed by [adb](https://developer.android.com/studio/command-line/adb) (probably, no root required, IDK). Show installed apps: `adb shell pm list packages`.  Remove a specific app: `adb shell pm uninstall -k --user 0 com.android.chrome`.
+ [fdroidcl](https://github.com/mvdan/fdroidcl) allows to install apps from [F-Droid](https://f-droid.org/).
+ Not everything is available on F-Droid, though. I often install such apps from [4pda](https://4pda.to/forum/index.php?showforum=212) (a Russian forum with apks, both official and modified ones) but there is no CLI for it. You can manually download the files and then install them using `adb install ./file.apk`.
+ You definitely shouldn't install bank apps from random people on Russian forums. So, for some apps you still need Google Play. For that, I use [gplaycli](https://github.com/matlink/gplaycli) but it took me a while to make it work, including fighting with 2FA and fixing some bits of the code.

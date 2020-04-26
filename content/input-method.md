Title: Setting up Alternate Input Methods on Linux
Date: 2020-04-26T19:26:59+00:00
Category: Computers
Tags: Software, Language
Slug: input-methods

I had never before had to set up an alternate input method for myself. However,
today, my wife asked me to help her do so.

An [input method][1] helps users type characters in other languages. Two
popular input method frameworks are [IBus][2] and [fcitx][3]. In this example,
I'll show how I got IBus working on a Debian-based distro.

1. Install IBus:

        :::text
        apt install ibus

2. [Optional] Install additional input methods, for example:

        :::text
        apt install ibus-cangjie ibus-zhuyin

    IBus appears to come with support for many western languages (French,
    German, Spanish, etc.) but not most non-Roman or non-Germanic lanuages,
    presumably because the libraries for these languages are probably much
    larger.

3. Configure IBus to enable the installed input methods by running

        :::text
        ibus-setup

    This will allow the user to select the input methods they wish to switch
    between and will also enable a hotkey (for example, Ctrl+space) to quickly
    switch between them.

4. Enable IBus to be run at login:

        :::text
        im-config -n ibus

    This sets IBus to run in your .xinputrc file. Presumably, this file is read
    by XOrg when starting to configure the input method. The contents of this
    file will probably be something like

        :::xorg.conf
        im_run ibus

    But I cannot verify this on my wife's machine right now because she is busy
    working.

5. Log out and log back in to ensure IBus is running. For some reason, I could
   not get it to work by just running `ibus`. Presumably, it is necessary to
   run it while XOrg is starting, not after it has already started.

At this point, it should work. Press the configured shortcut for switching
keyboards and see if the input has changed. There should also be a tray icon
that users can click to change the input method or configure settings.

[1]: https://en.wikipedia.org/wiki/Input_method
[2]: https://en.wikipedia.org/wiki/Intelligent_Input_Bus
[3]: https://en.wikipedia.org/wiki/Fcitx

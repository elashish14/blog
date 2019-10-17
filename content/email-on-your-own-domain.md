Title: Email on your own Domain
Date: 2019-10-16T03:57+00:00
Category: Computers
Tags: Software, Internet
Slug: email-on-your-own-domain

It has long been a priority of mine to migrate my email addresses to my own
domain name. My reasons for doing this are quite numerous:

1.  Email is probably our most intimate form of communication, and I am
    growing increasingly uncomfortable about using external services like
    Gmail to host it.

2.  Email has become extremely centralized, which can be dangerous for a
    standardized protocol. If a single entity has too much influence over
    important web standards, it enables them to manipulate said standards for
    their own benefit, potentially to the detriment of the public at large
    (see [1]).

3.  I am growing increasingly concerned about email providers imposing onerous
    requirements on setting up and accessing email accounts. Such requirements
    can include requiring users to provide a phone number, evaluate CAPTCHAs,
    or run non-free javascript.

4.  Internet giants (most notably Cloudflare) have been developing a
    reputation for being hostile to users who use technologies that enhance
    their privacy such as VPNs, Tor, anti-fingerprinting techniques, and
    others.

5.  Different providers may offer features with standard email providers do
    not. I'll detail some of the benefits of this setup further below.

6.  Having email on your own domain simply looks very cool.

However, setting up and managing an email server is not for the faint of
heart. Some drawbacks include:

1.  A misconfigured server can result in your domain being placed on a spam
    blacklist, and it can be extremely difficult to get off of these lists. If
    your domain ends up on one of these lists, messages that are sent to other
    users may never reach their inboxes.

2.  The server of course needs to be regularly updated with patches, and the
    domain must also not be allowed to expire. If a user's critical accounts
    are registered with said email address and the domain expires, a hacker
    could gain access to these accounts by registering the domain on their
    own, and then setting up their own mail server and triggering the password
    resets.

In the [next post][2], I'll explain the setup that I chose and how I implemented
it. It turned out to be a very easy process!

[1]: https://en.wikipedia.org/wiki/Embrace_extend_extinguish
[2]: email-with-gandi.html

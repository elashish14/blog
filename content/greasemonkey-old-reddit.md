Title: Switching to Old Reddit
Date: 2020-04-26T21:37:45+00:00
Category: Computers
Tags: WWW, Greasemonkey, Reddit
Slug: greasemonkey-old-reddit

[reddit.com][1] changed the interface of their website a year or two ago. I
won't go into more detailed criticism of the changes beyond saying that it
has a deficient level of information density for practical use.

After the change was introduced however, the previous styling could still be
accessed by changing URLs to the `old.reddit.com` subdomain. The website
provides a configuration setting for logged in users to set this permanently,
but this is problematic for a number of reasons. First, it has had a history of
issues and bugginess (which may be resolved now, but it is uncertain that all
use cases were caught). And second, this would obviously not work for anonymous
sessions without a significant amount of tedious manual changes.

So I wrote a Greasemokney script to resolve this. It provides a much more
robust solution to this issue:

    :::javascript
		// ==UserScript==
		// @name        Old reddit
		// @namespace   oldreddit
		// @include     *://reddit.com/*
		// @include     *://www.reddit.com/*
		// @include     *://reddit.com
		// @include     *://www.reddit.com
		// @version     1
		// @grant       none
		// ==/UserScript==

		window.location.replace(
			window.location.protocol + "//old.reddit.com" + window.location.pathname);

I'm aware that people typically share scripts like this on sites like
[greasyfork.org][2], but it's too much hassle to set up accounts for websites
these days.

[1]: http://old.reddit.com
[2]: https://greasyfork.org/

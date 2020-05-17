Title: Correcting Fixed Position Elements in the WWW
Date: 2020-05-17T19:34:48+00:00
Category: Computers
Tags: WWW, Greasemonkey
Slug: correct-fixed-position-elements

Floating elements are a new annoyance that web developers have decided to
adopt. For example, a web developer can write some CSS like this:

    :::css
    header {
        position: fixed; /* or sticky */
    }

This has the effect of preventing any elements matching the selector in
question from properly scrolling out of the browser viewport when the user
scrolls up or down. Here are a couple reasons why this is a bad practice:

* Scrolling becomes a very jarring experience since some portions of the page
  move properly while others don't

* These elements distract from the content of the page

* It is a waste of space

As a result, I'll share another Greasemonkey script that I use to correct the
CSS of these elements (which I borrowed from [here][1] and [here][2]).

    :::javascript
    // ==UserScript==
    // @name        Correct fixed position elements
    // @namespace   fixtheinternet
    // @include     *
    // @version     1
    // @run-at      document-end
    // @grant       none
    // ==/UserScript==

    function correct_fixed_elements() {
        try {
            var items = document.querySelectorAll('*');
            for (var i = items.length; i--;) {
                var elem = items[i];
                var props = window.getComputedStyle(elem, null);
                    if (props['position'] == 'fixed' || props['position'] == 'sticky') {
                        elem.style.cssText = 'position: static !important'
                    }
            }
        } catch(err) {
    //         alert(err);
        }
    }

    var timeout = 500;
    setTimeout(correct_fixed_elements, timeout);
    setTimeout(correct_fixed_elements, timeout * 3);
    setTimeout(correct_fixed_elements, timeout * 10);
    setTimeout(correct_fixed_elements, timeout * 30);

It iterates over all the elements on the DOM and gets the computed style
element of the element. If the computed `position` element of the style is
`fixed` or `sticky`, it is changed back to `static` as it should have been all
along. Some elements look better with `absolute` positioning instead, but it is
very difficult to determine which.

It's unfortunate that browsers aren't configurable enough to disable this
behaviour. We should be thankful though that HTML/CSS is sufficiently modular
enough to remedy these kinds of issues.

[1]: https://alisdair.mcdiarmid.org/kill-sticky-headers/
[2]: https://gist.github.com/alisdair/5670341

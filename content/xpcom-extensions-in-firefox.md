Title: XPCOM Extensions in Firefox
Date: 2020-08-21T12:25:10+00:00
Category: Computers
Tags: Software, WWW
Slug: xpcom-extensions-in-firefox

I read an [article][1] today about why Firefox had to get rid of XPCOM addons.
The article makes all the right technical arguments as to why Firefox had to
get rid of XPCOM extensions. And Mozilla were correct in the decision to do so
- the presence of XPCOM extensions was limiting the abilities Mozilla to
develop the core browser. Mozilla would certainly never have been able to
implement all of the performance and security features it has today if the core
developers were so hampered as they were by XPCOM. Yet nevertheless, most
people (correctly, in my opinion) feel that deprecating XPCOM was what caused
Firefox to become irrelevant.

But I disagree with most people as to *why* this is the case. Most people fail
to realise how important the extension community was to Firefox in its early
days. In those days, the browser was boring. [Internet Explorer 6][2] was the
only alternative to Firefox and aside from all of its quirks, incompatibilities
and security flaws, it was also a very boring and featureless browser. Firefox,
on the other hand, had a massive extension community behind it, and this was
the real source of innovation in the web browser. Here is just a short list of
some of the ground-breaking features the extension community developed:

* The first ever browser-based ad-blocker

* Firebug: the original DOM debugger

* The ability of users to inject their own CSS (Stylish) and Javascript
  (Greasemonkey), again, came from the extension community, not the browser
  developers.

* Many UI enhancements came from extensions, such as Tree-Style Tabs and the
  Statusbar Downloader. Tree-Style Tabs, for example, was so popular that
  Mozilla eventually had to relent and enable this behaviour post-XPCOM even
  though WebExtensions did not actually support it.

None of these features were developed by Mozilla. They were *enabled* by the
architecture that they supported, but it was the broader community that had
the ingenuity to implement them. And this was XPCOM's true power: the browser
wasn't held back by Mozilla's vision. XPCOM meant that anyone in the community
could innovate on what the browser could be. Deprecating XPCOM and leaving
extension developers with nothing be WebExtensions destroyed this source of
innovation and feature development. Or to put it another way, XPCOM meant
Firefox could be anything anyone wanted it to be; deprecating them meant that
Firefox could only be what Mozilla wanted it to be.

And this is the core problem. In a world with nothing but WebExtensions, it is
up to Mozilla to come up with all future innovation in Firefox. But it is
plainly evident that Mozilla has no idea what they think a browser ought to be
be. They copy one feature after another from Chrome and are constantly
rewriting the interface for components that are already done (the settings
dialog, DOM debugger, and so on). It was extension developers that gave
Mozilla direction and implemented most of the features that users actually
like! A few of the features extensions provided found their way into the core
browser (like re-opening recently closed tabs, which came from Tab Mix Plus,
Tree-Style Tabs, as mentioned above, and Firebug).

Now, I'm far from being in a position of telling Mozilla what to do, but I wish
they had done one of the following things:

1. Separate the browser and the rendering engine, so a broader community can
work toward real innovation in the browser while Mozilla retains their
expertise in developing what they are good at: a very good browser engine. My
understanding is that this is a work in progress.

2. Enhance WebExtensions so a broader community can continue to enhance the
browser and unlock its true potential. Easier said than done of course, but
it's probably a better spend of time than many of Mozilla's other projects.

And the phenomena which happened to Firefox are a microcosm of a more universal
truth: **the greatest progress is achieved when we empower as many people as
much as possible**. This is true not only in software but in all arts and
trades. And it is why open source products will always be better than their
closed counterparts.

So in summation, the only interesting features coming into Firefox were
extension developers; and Mozilla took this away when they deprecated XPCOM.
This is really what was a major loss, not just for Mozilla, but for the web as
a whole and all of its users. The browser is boring once again. The only new
developments are more harmful to users than helpful: removing the status bar,
obfuscating URLs, WebExtensions manifest v3, DRM, and the removal of many more
settings and features. Mozilla will be powerless to save the open web if it
does not embrace a larger community.

[1]: https://yoric.github.io/post/why-did-mozilla-remove-xul-addons/
[2]: https://en.wikipedia.org/wiki/Internet_Explorer_6

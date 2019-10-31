#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ashish Banerjee'
SITENAME = "Ashish Banerjee's Website"
SITEURL = 'http://ashishbanerjee.net/site'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('C.W. Taekwondo (requires Javascript to view)', 'https://www.cwtkd.com/'),
         ('/r/dota2', 'https://old.reddit.com/r/DotA2/'),
         ('Dota VODs', 'https://old.reddit.com/r/DotaVods/'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'theme/notmyidea-blue'

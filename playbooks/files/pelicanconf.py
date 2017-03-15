#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Antonio Alaniz'
SITENAME = 'Adventures in Python, Javascript, Ruby and C'
SITEURL = 'antonioalaniz.com'
# This needs to be a variable for Ansible
THEME = '/home/talaniz/pelican-themes/pelican-clean-blog'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Sandwichheat'),
          ('LinkedIn', 'https://www.linkedin.com/in/antonioalaniz'),
          ('GitHub', 'https://github.com/talaniz/'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

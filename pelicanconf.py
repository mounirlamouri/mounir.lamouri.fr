#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Mounir Lamouri'
SITENAME = "Mounir Lamouri's Blog"
SITEURL = ''

THEME = 'theme'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

ARTICLE_URL='{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS='{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL='{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS='{date:%Y}/{date:%m}/{slug}-{lang}.html'

FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

TEMPLATE_PAGES = { 'static/resume.html': '/resume.html' }

# Feeds settings.
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = False

# For planets plugin.
PLANET_FEED_ATOM = "feeds/planet.%s.atom.xml"
import sys;
sys.path.append('plugins')
PLUGINS = [ 'planets' ]

# Not using those for the moment.
LINKS =  ()
SOCIAL = ()

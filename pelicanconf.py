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

# Feeds settings.
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = False

# Not using those for the moment.
LINKS =  ()
SOCIAL = ()

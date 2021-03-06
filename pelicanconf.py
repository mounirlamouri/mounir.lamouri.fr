#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Mounir Lamouri'
SITENAME = "Mounir Lamouri's Blog"
SITEURL = ''

THEME = 'theme'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

ARTICLE_URL='{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS='{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL='{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS='{date:%Y}/{date:%m}/{slug}-{lang}.html'

#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
STATIC_PATHS = [
    'extra/robots.txt',
    'images',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

READERS = { 'html': None }
TEMPLATE_PAGES = { 'static/resume.html': 'resume.html' }

# Feeds settings.
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = False

# Not using those for the moment.
LINKS =  ()
SOCIAL = ()

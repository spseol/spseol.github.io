#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'spseol.cz'
SITENAME = u'spseol.github.io'
# SITEURL = 'spseol.github.io'
# SITEURL = ''

PATH = 'content'
THEME = 'themes/simplegrey'
TIMEZONE = 'Europe/Prague'

TYPOGRIFY = True

DEFAULT_LANG = u'cz'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('github.com/spseol', 'https://github.com/spseol/'),
         ('www.spseol.cz', 'http://www.spseol.cz/'),
         ('~nozka', 'http://hroch.spseol.cz/~nozka/'),
         ('Pelican', 'http://blog.getpelican.com/'),
         )

# Social widget
SOCIAL = (('GitHub', 'https://github.com/spseol/'),
          ('Facebook', 'https://cs-cz.facebook.com/spseol'),
          ('G+', 'https://plus.google.com/118347382558771670752'),
          )

DEFAULT_PAGINATION = False


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MD_EXTENSIONS = [
    'codehilite(css_class=highlight)',
    'extra',
    'headerid(level=2)',
    'toc',
    'linksShortcuts:Shortcuts',
]

#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import time

LAST_UPDATE = str(time.strftime('%m %Y'))
YEAR = str(time.strftime('%Y'))

SITEURL = ''
AUTHOR = u'Polis Labs'
AUTHOR_LINKS = {
    'GITHUB' : 'https://github.com/polislabs',
    'TWITTER' : 'http://twitter.com/polislabs/',
    # use html entities to obfuscate for spammers (http://stackoverflow.com/questions/748780/best-way-to-obfuscate-an-e-mail-address-on-a-website)
    'EMAIL' : '&#106;&#111;&#101;&#064;&#112;&#111;&#108;&#105;&#115;&#108;&#097;&#098;&#115;&#046;&#111;&#114;&#103;'
}
SITENAME = u'Polis Labs'
SITESUBTITLE = u''

NAV_PAGES = []

THEME = 'themes/polis/'

PATH = 'content'

TIMEZONE = 'US/Mountain'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%Y-%B-%d'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives','sitemap')

SITEMAP_SAVE_AS = 'sitemap.xml'

STATIC_PATHS = []
PLUGIN_PATHS = ["plugins", 'plugins/pelican-plugins']
PLUGINS = [
            'assets',
            ]
# PLUGIN Settings
GITHUB_USER = 'polislabs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'archive/{slug}/'
ARTICLE_SAVE_AS = 'archive/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
#CATEGORY_URL = 'category/{slug}/'
#CATEGORY_SAVE_AS = 'category/{slug}/index.html'
#TAG_URL = ''
#TAG_SAVE_AS = ''
#AUTHOR_URL = ''
#AUTHOR_SAVE_AS = ''
ARCHIVES_URL = 'archive/'
ARCHIVES_SAVE_AS = 'archive/index.html'
#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


COPYRIGHT_LINK = 'http://creativecommons.org/licenses/by-nc-nd/4.0/'

#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'FiftysixTimes7'
SITENAME = '世界观察日记'
# SITEURL = 'https://fiftysixtimes7.github.io/MyWorldObservationJournal'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh-cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

LINKS = (('source', 'https://github.com/FiftysixTimes7/MyWorldObservationJournal'),
         ('issues', 'https://github.com/FiftysixTimes7/MyWorldObservationJournal/issues'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


DEFAULT_DATE_FORMAT = '%x %a'
THEME = 'pelican-alchemy/alchemy'
SITEIMAGE = 'images/profile.png'
HIDE_AUTHORS = True
SITESUBTITLE = 'Written by FiftysixTimes7'
ICONS = (('github', 'https://github.com/FiftysixTimes7'),)
THEME_TEMPLATES_OVERRIDES = ['theme-patch']
FILENAME_METADATA = r'(?P<date>\d{4}\d{2}\d{2}T\d{2}\d{2})_(?P<title>.*)'
EXTRA_PATH_METADATA = {'images/favicon.ico': {'path': 'favicon.ico'}}

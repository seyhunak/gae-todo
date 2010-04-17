# -*- coding: utf-8 -*-
import os
from django.utils.translation import ugettext as _
from ragendja.settings_pre import *
from django.conf import settings

# load appsettings
try:
  from app_settings import *
except ImportError:
  pass

# Debugging
DEBUG = False
APPEND_SLASH=False 

# address settings
FULL_URL = 'http://notalma.appspot.com'

# Google account settings
AUTH_ADMIN_USER_AS_SUPERUSER = False
AUTH_USER_MODULE = 'ragendja.auth.hybrid_models'

# Email account settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'xxxxxxxxx'
EMAIL_PORT = 587
    
#feeds settings
FEEDS_AUTHOR= 'Todo'
FEEDS_EMAIL= 'youremail@gmail.com'
POSTS_PER_FEED = 10

# cache backend
CACHE_BACKEND = 'memcached://'

# Increase this when you update your media on the production site, so users
# don't have to refresh their cache. By setting this your MEDIA_URL
# automatically becomes /media/MEDIA_VERSION/
MEDIA_VERSION = 1
DJANGO_STYLE_MODEL_KIND = False

# By hosting media on a different domain we can get a speedup (more parallel
# browser connections).
#if on_production_server or not have_appserver:
#    MEDIA_URL = 'http://media.mydomain.com/media/%d/'

# Add base media (jquery can be easily added via INSTALLED_APPS)
COMBINE_MEDIA = {
    'combined-%(LANGUAGE_CODE)s.js': (
        # See documentation why site_data can be useful:
        # http://code.google.com/p/app-engine-patch/wiki/MediaGenerator
        '.site_data.js',
        'global/application.js',        
    ),
    'combined-%(LANGUAGE_DIR)s.css': (        
        'global/application.css',
    ),
}

# Change your email settings
if on_production_server:
    DEFAULT_FROM_EMAIL = 'youremail@gmail.com'
    SERVER_EMAIL = DEFAULT_FROM_EMAIL

# email server settings
ACCOUNT_ACTIVATION_DAYS=7
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER='youremail@gmail.com'
EMAIL_HOST_PASSWORD='xxxxxxxxxxxx'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'youremail@gmail.com'
SERVER_EMAIL = 'youremail@gmail.com'
ADMINS = (('Yourname', 'youremail@gmail.com'), \
          ('Yourname', 'youremail@gmail.com'))

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1234567890'

#ENABLE_PROFILER = True
#ONLY_FORCED_PROFILE = True
#PROFILE_PERCENTAGE = 25
#SORT_PROFILE_RESULTS_BY = 'cumulative' # default is 'time'
# Profile only datastore calls
#PROFILE_PATTERN = 'ext.db..+\((?:get|get_by_key_name|fetch|count|put)\)'

# Enable I18N and set default language to 'en'
USE_I18N = True
LANGUAGE_CODE = 'en'

# Restrict supported languages (and JS media generation)
# Initalizing Gettext
gettext = lambda s: s

# Valid languages
LANGUAGES = (
    ('en', gettext('English')),
    ('tr', gettext('Türkçe')),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'ragendja.template.app_prefixed_loader',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'ragendja.auth.context_processors.google_user',
     # App
    'todo.context_processors.full_url',
    'todo.context_processors.current_user',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'ragendja.middleware.ErrorMiddleware',
    'ragendja.middleware.LoginRequiredMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',                      
    # Django authentication
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Google authentication
    'ragendja.auth.middleware.GoogleAuthenticationMiddleware',
    # Hybrid Django/Google authentication
    'ragendja.auth.middleware.HybridAuthenticationMiddleware',  
    'ragendja.sites.dynamicsite.DynamicSiteIDMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
)

# Google authentication
#AUTH_USER_MODULE = 'ragendja.auth.google_models'
#AUTH_ADMIN_MODULE = 'ragendja.auth.google_admin'
# Hybrid Django/Google authentication
AUTH_USER_MODULE = 'ragendja.auth.hybrid_models'

GLOBALTAGS = (
    'ragendja.templatetags.ragendjatags',
    'django.templatetags.i18n',
    # 'ragendja.templatetags.googletags',
    'todo.templatetags.menu',
    'todo.templatetags.common',
    'todo.templatetags.gravatar',
    'todo.templatetags.tags',
    'todo.templatetags.pygmentize',
)

LOGIN_REDIRECT_URL = '/todo/'
LOGIN_REQUIRED_PREFIXES = (
    '/todo/'
)
NO_LOGIN_REQUIRED_PREFIXES = (
    '/',
)

# Captcha
NUMBERS = getattr(settings, 'MATH_CAPTCHA_NUMBERS', range(1,6))
OPERATORS = getattr(settings, 'MATH_CAPTCHA_OPERATORS', '-+')
QUESTION = getattr(settings, 'MATH_CAPTCHA_QUESTION', 'What is output? ')

INSTALLED_APPS = (
    # Add jquery support (app is in "common" folder). This automatically
    # adds jquery to your COMBINE_MEDIA['combined-%(LANGUAGE_CODE)s.js']
    # Note: the order of your INSTALLED_APPS specifies the order in which
    # your app-specific media files get combined, so jquery should normally
    # come first.

    # JQuery framework
    'jquery',
    # Blueprint CSS framework (http://blueprintcss.org/)
    'blueprintcss',
    
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.sitemaps',
    'appenginepatcher',
    'ragendja',
    'todo',
    'search',
    'mediautils',
)


# List apps which should be left out from app settings and urlsauto loading
IGNORE_APP_SETTINGS = IGNORE_APP_URLSAUTO = (
    # Example:
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'yetanotherapp',
)

# Remote access to production server (e.g., via manage.py shell --remote)
DATABASE_OPTIONS = {
    # Override remoteapi handler's path (default: '/remote_api').
    # This is a good idea, so you make it not too easy for hackers. ;)
    # Don't forget to also update your app.yaml!
    #'remote_url': '/remote-secret-url',

    # !!!Normally, the following settings should not be used!!!

    # Always use remoteapi (no need to add manage.py --remote option)
    #'use_remote': True,

    # Change appid for remote connection (by default it's the same as in
    # your app.yaml)
    #'remote_id': 'otherappid',

    # Change domain (default: <remoteid>.appspot.com)
    #'remote_host': 'bla.com',
}

from ragendja.settings_post import *

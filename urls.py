# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from ragendja.urlsauto import urlpatterns
from ragendja.auth.urls import urlpatterns as auth_patterns
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
admin.autodiscover()
handler500 = 'ragendja.views.server_error'

urlpatterns = auth_patterns + patterns('',
    ('^admin/(.*)', admin.site.root),
    (r'^$', 'django.views.generic.simple.direct_to_template',
        {'template': 'main.html'}), 
    (r'contact/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'contact.html'}), 
    (r'terms/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'terms.html'}), 
    (r'privacy/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'privacy.html'}),
    (r'robots.txt$', 'django.views.generic.simple.direct_to_template',
        {'template': 'robots.txt'}),
) + urlpatterns

# I18N for Python and Template Code
urlpatterns += patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),
)

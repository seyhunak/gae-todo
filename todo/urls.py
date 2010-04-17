# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse

urlpatterns = patterns('todo.views',
    (r'^$', 'list_todo'), 
    (r'^add/$', 'add_todo'), 
    (r'^delete/(?P<key>.+)$', 'delete_todo'),
    (r'^post/$', 'post_todo'),
    (r'^update_position/$', 'update_position_todo'),
    (r'^update_text/$', 'update_text'),
)

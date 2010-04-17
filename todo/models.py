# -*- coding: utf-8 -*-
# imports
from django.db.models.signals import post_save,pre_delete,post_delete
from django.db.models import signals,permalink
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import force_unicode,smart_str
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from google.appengine.ext import db
from google.appengine.api import users
from ragendja.dbutils import cleanup_relations
from search.core import SearchIndexProperty, porter_stemmer
import re
import unicodedata

COLOR_CHOICES = (
    ('yellow'),
    ('blue'),
    ('green'),
)

class Todo(db.Model):
    user = db.ReferenceProperty(User, required=False, collection_name='todo')
    name = db.StringProperty(required=False)  
    text = db.StringProperty(required=False)  
    color = db.StringProperty(choices=COLOR_CHOICES)
    x = db.IntegerProperty(required=False)  
    y = db.IntegerProperty(required=False)  
    z = db.IntegerProperty(required=False)  
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return str(self.name)
 

    def get_url(self):
        return "/%s" % self.key

    @permalink
    def get_absolute_url(self):
        return ('todo.views.show_todo', (), {'key': self.key()})

    # index used to retrieve posts using the title, content or the
    # category as whole words
    search_index = SearchIndexProperty(('name'), indexer=porter_stemmer, relation_index=False)    


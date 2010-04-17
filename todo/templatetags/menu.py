import urllib, hashlib
from django.template import Library, Node
from django.contrib.flatpages.models import FlatPage
from django.template.defaultfilters import stringfilter
from django import template
from google.appengine.ext import db
register = template.Library()

def menu():
    flatpages = FlatPage.all().order('title')
    if flatpages:
      for i in range(len(flatpages)):
        menu = '<a href="'+flatpages[i].url+'" title="'+flatpages[i].title+'">'+flatpages[i].title+'</a>'
      return menu 
register.simple_tag(menu)

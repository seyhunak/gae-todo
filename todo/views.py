# -*- coding: utf-8 -*-
import datetime
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django import http
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, delete_object, \
    update_object
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from google.appengine.ext import db
from mimetypes import guess_type
from ragendja.dbutils import get_object_or_404, get_object, get_object_list
from ragendja.template import TextResponse, render_to_string, render_to_response
from todo.commons import *
from todo.forms import make_todo_form
from todo.models import Todo

def list_todo(request):
    user = request.user
    if user.is_authenticated():
      todos = get_object_list(Todo, "user =", user.key()).fetch(999)     
      return render_to_response(request, 'todo_list.html', {'todos':paginate(request, todos)}) 
    else:
      return HttpResponseRedirect('http://localhost:8000/_ah/login?continue=http://notalma.appspot.com')
      
def add_todo(request):
   user = request.user
   if user.is_authenticated():      
        return render_to_response(request, 'todo_add.html') 

def delete_todo(request, key):
    user = request.user
    if user.is_authenticated():
      try:
        todo = get_object(Todo, key)
        todo.delete()
        return HttpResponseRedirect('/todo/')
      except KeyError:
        pass
    else:
        return HttpResponseRedirect('/todo/')
        
def post_todo(request):
    user = request.user
    if user.is_authenticated():    
        name = request.POST.get('author')
        text = request.POST.get('body')
        color = request.POST.get('color')      
        todo = Todo(user=user,name=name,text=text,color=color,x=156,y=138,z=100)
        todo.save()      
        return HttpResponse('29')      
                   
def update_position_todo(request):   
    user = request.user
    if user.is_authenticated():
      try:
        todo = Todo.get_by_id(int(request.GET.get('id')))
        todo.x =  int(request.GET.get('x'))
        todo.y =  int(request.GET.get('y'))
        todo.z =  int(request.GET.get('z'))
        todo.put()
        return HttpResponseRedirect('/todo/')
      except KeyError:
        pass
    else:
        return HttpResponseRedirect('/todo/')
        
def update_text(request):   
    user = request.user
    if user.is_authenticated():
        post = request.POST.copy() 
        todo = Todo.get_by_id(int(request.POST.get('id')))
        todo.text = post['value'] 
        todo.put()
        return render_to_response(request, 'todo_changed.html', {'todo': todo})
    else:
        return HttpResponseRedirect('/todo/')

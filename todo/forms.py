# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from todo.models import Todo

def make_todo_form(request):
    class TodoForm(forms.ModelForm):
        class Meta:
            model = Todo
            fields = ['name','text','color']

        def save(self, commit=True):
            f = super(TodoForm, self).save(commit=False)
            if not f.pk: f.user = request.user
            if commit: f.save()
            return f

    return TodoForm

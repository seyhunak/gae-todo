# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
import re

_IPHONE_UA = re.compile(r'Mobile.*Safari')
def is_iphone(request):
    return _IPHONE_UA.search(request.META['HTTP_USER_AGENT']) is not None

def response(template,*args):
    def _process_view(view_func):
        def _handle_request(request,*args,**kwargs):
            context = view_func(request,*args,**kwargs)
            if context is None: context = dict()
            if isinstance(context,dict):
                path = is_iphone(request) and 'iphone' or 'web'
                return render_to_response('%s/%s' % (path,template),RequestContext(request,dict=context))
            else:
                return context #this is probably a redirect

        return _handle_request
    return _process_view

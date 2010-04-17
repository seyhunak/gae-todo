# -*- coding: utf-8 -*-
from django.core.paginator import Paginator,InvalidPage, EmptyPage
def paginate(request, objects, count=10, param_name='page'):
    """
    Shortcut for paginating by some object
    """
    paginator = Paginator(objects, count)

    try:
        pagenum = int(request.GET.get('%s' % param_name, '1'))
    except ValueError:
        pagenum = 1
    
    try:
        result = paginator.page(pagenum)
    except (EmptyPage, InvalidPage):
        result = paginator.page(paginator.num_pages)
    
    return result

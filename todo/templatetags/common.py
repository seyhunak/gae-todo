from django.template import Library, Node
from django.db.models import get_model
from ragendja.dbutils import get_object_list
from google.appengine.ext import db
from google.appengine.api import memcache
import logging

register = Library()
     
class LatestContentNode(Node):
    def __init__(self, model, num, varname, cache_key = None):
        self.num, self.varname, self.cache_key = int(num), varname, cache_key
        self.model = get_model(*model.split('.'))
    
    def render(self, context):
        #items = self.model._default_manager.all().order('-created').filter("published = ", True)[:self.num]
        #items = get_object_list(self.model, "published = ", True).order('-created').fetch(self.num)
        #items = get_object_list(self.model).fetch(self.num)
        items = memcache.get(self.cache_key)
        
        if items is None:
          items = db.Query(self.model).order('-created').filter("published = ", True).fetch(self.num)
          if not memcache.add(self.cache_key, items, 3600):
            logging.error("Memcache set failed.")
        newlist = []
        
        for i in range(0, len(items), 3):
          newlist.append({str(i): items[i:(i+3)]})

        context[self.varname] = newlist
        
        return ''
 
def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) != 6:
        raise TemplateSyntaxError, "get_latest tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest tag must be 'as'"
    return LatestContentNode(bits[1], bits[2], bits[4], bits[5])

class LatestCategoryNode(Node):
    def __init__(self, model, category, varname):
        self.category, self.varname = category, varname
        self.model = get_model(*model.split('.'))
    
    def render(self, context):
        category_model = 'myblog.Categoria'
        Categoria = get_model(*category_model.split('.'))
        categoria = db.Query(Categoria).filter("name =", self.category).get()
        
        if categoria:
          #items = db.Query(self.model).order('-created').filter("category = ", categoria.key()).filter("published = ", True).get()
          items = db.Query(self.model).filter("category = ", categoria.key()).filter("published = ", True).get()
          
          if items:
            img_model = 'myblog.File'
            File = get_model(*img_model.split('.'))
            items.image = db.Query(File).filter("news =", items.key()).get()
          
        else:
          items = None
          
        context[self.varname] = items
        return ''
 
def get_latest_by_cat(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest tag must be 'as'"
    return LatestCategoryNode(bits[1], bits[2], bits[4])

@register.filter
def tabularize(value, cols):
    '''
        modifies a list to become a list of lists 
        eg [1,2,3,4] becomes [[1,2], [3,4]] with an argument of 2
        Taken from django user group

        Usage:
          {% for row in object_list|tabularize:"4" %}
            {% for obj in row %}
              ....
            {% endfor %}
          {% endfor %}
    '''
    try:
        cols = int(cols)
    except ValueError:
        return [value]

    return map(*([None] + [value[i::cols] for i in range(0, cols)]))

get_latest = register.tag(get_latest)
get_latest_by_cat = register.tag(get_latest_by_cat)


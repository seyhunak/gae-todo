from django.template import Library, Node
from myapp.models import Tag
from google.appengine.ext import db
register = Library()

class TagsCloudNode(Node):

    def __init__(self, num, context_var):
        self.context_var = context_var
        self.num = int(num)
        
    def sort_by_attr(self,seq,attr):
        intermed = [ (getattr(seq[i],attr), i, seq[i]) for i in xrange(len(seq)) ]
        intermed.sort()
        return [ tup[-1] for tup in intermed ]

    def gen_cloud(self, num):
        query=Tag.all().filter("count >", 0).order('-count')
        p = query.fetch(num)
        if p:
            max1=max([int(p_item.post_count) for p_item in p])

        for i in range(len(p)):
            size =int(round(int(p[i].post_count)*maxsize/max1))
            if size<minsize:
                size=minsize
            cloudsize =str(size) +"%"
            p[i].cloudsize=cloudsize
        return self.sort_by_attr(p, "label")

    def render(self, context):
        context[self.context_var] = self.gen_cloud(self.num)
        return ''


def get_tags_cloud(parser, token):
    bits = token.contents.split()
    if len(bits) != 4:
        raise template.TemplateSyntaxError("'%s' tag takes exactly three arguments" % bits[0])
    if bits[2] != 'as':
        raise template.TemplateSyntaxError("second argument to '%s' tag must be 'as'" % bits[0])

    return TagsCloudNode(bits[1], bits[3])
get_tags_cloud= register.tag(get_tags_cloud)

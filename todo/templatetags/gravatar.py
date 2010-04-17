from django import template
import urllib, hashlib
register = template.Library()

# Adapted and updated from http://www.djangosnippets.org/snippets/772/
# Usage: {% gravatar foo@bar.com %} or {% gravatar foo@bar.com 40 R http://foo.com/bar.jpg %}
def gravatar(email, size=50, rating='g', default_image=''):
    gravatar_url = "http://www.gravatar.com/avatar/"
    gravatar_url += hashlib.md5(email).hexdigest()
    gravatar_url += '?' + urllib.urlencode({'s':str(size),
        'r':rating,
        'd':default_image})
    return """<img style="float:left; margin:4px 8px 8px 4px" src="%s" alt="gravatar" />""" % gravatar_url

register.simple_tag(gravatar)

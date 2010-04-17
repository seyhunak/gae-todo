from django.contrib.auth.models import User
from ragendja.dbutils import get_object_or_404, get_object, get_object_list
from google.appengine.ext import db

def full_url(request):
    from django.conf import settings
    return {'FULL_URL': settings.FULL_URL}
    
def current_user(request):
    user = request.user
    if user:
      return {'current_user': user}

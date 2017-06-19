from django.conf.urls import url
from blog.views import *
 
urlpatterns = [
    url(r'^$', post_list),
    url(r'^(?P<id>\d+)/$', post_detail),
]
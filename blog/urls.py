
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', get_main, name="mainblog"),
    url(r'^post/(\d+)', get_blog, name="blog"),
    url(r'^edit/(\d+)', edit_blog, name="edit"),
    url(r'^delete/(\d+)', delete_blog, name="delete"),
    url(r'^delete/confirm/(\d+)', delete_confirm, name="deleteconfirm"),
    url(r'^write/', write_blog, name="write"),
    url(r'^publish/(\d+)', publish, name="publish"),
    
]
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^logout/', logout, name='logout'),
    url(r'^login/', login, name='login'),
    url(r'^yourprofile/', yourprofile, name='yourprofile'),
    url(r'^profile/(\d+)/', profile, name='profile'),
    url(r'^register/', register, name='register'),
]
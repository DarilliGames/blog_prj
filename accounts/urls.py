from django.conf.urls import url, include
from .views import *
from . import urlsreset

urlpatterns = [
    url(r'^logout/', logout, name='logout'),
    url(r'^login/', login, name='login'),
    url(r'^yourprofile/', yourprofile, name='yourprofile'),
    url(r'^profile/(\d+)/', profile, name='profile'),
    url(r'^register/', register, name='register'),
    url(r'^delete/(\d+)', remove_profile, name='deleteaccount'),
    url(r'^password-reset/', include(urlsreset)),
]
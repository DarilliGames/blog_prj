from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', get_inbox, name="inbox"),
    url(r'^sent/', get_sent, name="sent"),
    url(r'^mail/(\d+)', get_mail, name="mail"),
    url(r'^write/', write_mail, name="write"),
   url(r'^send/', send, name="send"),
]
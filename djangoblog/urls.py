from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings

import home.views as home_views

from accounts import urls as accounts_urls
from blog import urls as blog_urls
from mbox import urls as mail_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_index, name="home"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^messenger/', include(mail_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]

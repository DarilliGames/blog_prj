from django.conf.urls import url, include
from django.contrib import admin

import home.views as home_views

from accounts import urls as accounts_urls
from blog import urls as blog_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_index, name="home"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^blog/', include(blog_urls)),
]

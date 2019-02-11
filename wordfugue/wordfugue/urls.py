from django.conf.urls import url, include
from django.contrib import admin
from blog.feeds import BlogFeed
from home.views import HomeView

from django.urls import path, re_path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^$", HomeView.as_view(), name="home"),
    url(r"^feed/", BlogFeed()),
    url(r"^p/", include("django.contrib.flatpages.urls")),
    url(r"^talks/", include("talks.urls", namespace="talks")),
    re_path(r"^cms/", include(wagtailadmin_urls)),
    re_path(r"^documents/", include(wagtaildocs_urls)),
    re_path(r"^pages/", include(wagtail_urls)),
    url(r"^", include("blog.urls", namespace="blog")),
]

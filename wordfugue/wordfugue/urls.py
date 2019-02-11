from django.conf.urls import url, include
from django.contrib import admin
from blog.feeds import BlogFeed
from home.views import HomeView

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^$", HomeView.as_view(), name="home"),
    url(r"^feed/", BlogFeed()),
    url(r"^p/", include("django.contrib.flatpages.urls")),
    url(r"^talks/", include("talks.urls")),
    url(r"^", include("blog.urls")),
]

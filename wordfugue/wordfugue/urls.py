from django.conf.urls import url, include
from django.contrib import admin
from home.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^p/', include('django.contrib.flatpages.urls')),
    url(r'^', include('blog.urls', namespace='blog')),
]

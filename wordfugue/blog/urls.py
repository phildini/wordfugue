from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.BlogPostView.as_view(), name="post")
]
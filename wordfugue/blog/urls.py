from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.BlogPostView.as_view(), name="post"),
    url(r'^preview/(?P<slug>[\w-]+)/$', views.BlogPostPreviewView.as_view()),
    url(r'^tag/(?P<slug>[\w-]+)/$', views.TaggedPostView.as_view()),
]
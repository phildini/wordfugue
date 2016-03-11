from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.BlogPostView.as_view(), name="post"),
    url(r'^preview/(?P<slug>[\w-]+)/$', views.BlogPostPreviewView.as_view()),
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.TalkView.as_view(), name="talk"),
    url(r'^$', views.TalkListView.as_view(), name='list'),
    url(r'^tag/(?P<slug>[\w-]+)/$', views.TaggedTalkView.as_view()),
]
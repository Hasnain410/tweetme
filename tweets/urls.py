from django.conf.urls import url
from django.urls import path
from .views import (
TweetCreateView,
TweetListView,
TweetDetailView,
)

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'), # /tweet/
    path('create/', TweetCreateView.as_view(), name='create'), # /tweet/create/
    #url(r'^create/$', TweetCreateView.as_view(), name='create'), # /tweet/create/
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
]

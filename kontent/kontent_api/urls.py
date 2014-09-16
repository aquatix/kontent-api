from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, url, include
from rest_framework import viewsets

urlpatterns = patterns(
        '',
        url(r'^authenticate/', obtain_auth_token, name='authenticate'),
        url(r'^sites/(?P<pk>.+)/$', views.SiteDetail.as_view(), name='site-detail'),
        url(r'^sites/$', views.SiteList.as_view(), name='site-list'),
)

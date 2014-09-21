from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, url, include
from rest_framework import viewsets
from . import views

urlpatterns = patterns(
        '',
        #url(r'^authenticate/', obtain_auth_token, name='authenticate'),
        url(r'^sites/(?P<pk>.+)/$', views.SiteDetail.as_view(), name='site-detail'),
        url(r'^sites/$', views.SiteList.as_view(), name='site-list'),
        url(r'^sites/(?P<site_pk>.+)/groups/(?P<pk>.+)/$', views.ContentGroupDetail.as_view(), name='contentgroup-detail'),
        url(r'^sites/(?P<site_pk>.+)/groups/$', views.ContentGroupList.as_view(), name='contentgroup-list'),
        url(r'^accounts/(?P<pk>.+)/$', views.KontentUserDetail.as_view(), name='kontentuser-detail'),
        url(r'^accounts/$', views.KontentUserList.as_view(), name='kontentuser-list'),
        url(r'^items/(?P<pk>.+)/$', views.ContentItemDetail.as_view(), name='contentitem-detail'),
        url(r'^items/$', views.ContentItemList.as_view(), name='contentitem-list'),
)

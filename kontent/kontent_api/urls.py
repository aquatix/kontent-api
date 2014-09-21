from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, url, include
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'sites', views.SiteViewSet)

urlpatterns = patterns(
        '',
        #url(r'^authenticate/', obtain_auth_token, name='authenticate'),
        url(r'^sites/(?P<pk>.+)/$', views.SiteViewSet.as_view(), name='site-detail'),
        url(r'^sites/$', views.SiteViewSet.as_view(), name='site-list'),
        url(r'^sites/(?P<site_pk>.+)/groups/(?P<pk>.+)/$', views.ContentGroupDetail.as_view(), name='contentgroup-detail'),
        url(r'^sites/(?P<site_pk>.+)/groups/$', views.ContentGroupList.as_view(), name='contentgroup-list'),
)

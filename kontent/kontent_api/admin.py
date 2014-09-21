from django.contrib import admin
from django.db import models
from .models import (
        KontentUser,
        Site,
        ContentGroup)


class KontentUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ['name', 'user']


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


class ContentGroupAdmin(admin.ModelAdmin):
    #list_display = ('name', 'parent')
    #list_display = ('site')
    list_display = ('name',)


admin.site.register(KontentUser, KontentUserAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(ContentGroup, ContentGroupAdmin)

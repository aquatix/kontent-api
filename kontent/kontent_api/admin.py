from django.contrib import admin
from .models import (
        Site,
        ContentGroup)

class SiteAdmin(admin.SiteAdmin):
    list_display = ('title',)
    search_fields = ['title',]


class ContentGroupAdmin(admin.ContentGroupAdmin):
    list_display = ('title',)
    search_fields = ['title',]


admin.site.register(Site, SiteAdmin)
admin.site.register(ContentGroup, ContentGroupAdmin)

from django.contrib.auth.models import User, Group
from rest_framework import serializers
import markdown
from django.utils.safestring import mark_safe
from .models import (
        KontentUser,
        Site,
        ContentGroup,
        ContentObject,
        ContentItem)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'title')


class KontentUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KontentUser


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site


class ContentGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentGroup


class ContentItemSerializer(serializers.HyperlinkedModelSerializer):
    body = serializers.CharField()
    body_html = serializers.CharField(source='body', read_only=True)

    def transform_body_html(self, obj, value):
        return mark_safe(markdown.markdown(value))

    class Meta:
        model = ContentItem

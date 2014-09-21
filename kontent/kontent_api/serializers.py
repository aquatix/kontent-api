from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import (
        KontentUser,
        Site,
        ContentGroup,
        ContentObject)


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


class TextItem(serializers.HyperlinkedModelSerializer):
    body = serializers.TextField()
    body_html = serializers.TextField(source='body', read_only=True)

    def transform_body_html(self, obj, value):
        from django.contrib.markup.templatetags.markup import markdown
        return markdown(value)

    class Meta:
        model = TextItem

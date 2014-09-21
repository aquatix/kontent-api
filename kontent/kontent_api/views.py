from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import (
        UserSerializer,
        GroupSerializer,
        SiteSerializer,
        ContentGroupSerializer)
from .models import (
        KontentUser,
        Site,
        ContentGroup,
        ContentObject)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sites to be viewed or edited.
    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class ContentGroupList(viewsets.ModelViewSet):
    """
    API endpoint that allows lists of ContentGroups to be viewed or edited.
    """
    queryset = ContentGroup.objects.all()
    serializer_class = ContentGroupSerializer


class ContentGroupDetail(viewsets.ModelViewSet):
    """
    API endpoint that allows ContentGroups to be viewed or edited.
    """
    queryset = ContentGroup.objects.all()
    serializer_class = ContentGroupSerializer

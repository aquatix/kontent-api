from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics
from .serializers import (
        UserSerializer,
        GroupSerializer,
        KontentUserSerializer,
        SiteSerializer,
        ContentGroupSerializer,
        ContentItemSerializer)
from .models import (
        KontentUser,
        Site,
        ContentGroup,
        ContentObject,
        ContentItem)


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


class KontentUserList(generics.ListCreateAPIView):
    """
    API endpoint that allows lists of authors/owners to be viewed or edited.
    """
    queryset = KontentUser.objects.all()
    serializer_class = KontentUserSerializer


class KontentUserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows an author/owner to be viewed or edited.
    """
    queryset = KontentUser.objects.all()
    serializer_class = KontentUserSerializer


class SiteList(generics.ListAPIView):
    """
    API endpoint that allows lists of Sites to be viewed or edited.
    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class SiteDetail(generics.RetrieveAPIView):
    """
    API endpoint that allows Sites to be viewed or edited.
    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class ContentGroupList(generics.ListCreateAPIView):
    """
    API endpoint that allows lists of ContentGroups to be viewed or edited.
    """
    queryset = ContentGroup.objects.all()
    serializer_class = ContentGroupSerializer


class ContentGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows ContentGroups to be viewed or edited.
    """
    queryset = ContentGroup.objects.all()
    serializer_class = ContentGroupSerializer


class ContentItemList(generics.ListCreateAPIView):
    """
    API endpoint that allows lists of ContentItems to be viewed or edited.
    """
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer


class ContentItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows ContentItems to be viewed or edited.
    """
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer


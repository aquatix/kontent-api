from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ('-date_created', )


class KontentUser(BaseModel):
    user = models.OneToOneField(User, related_name='authuser')
    name = models.CharField(max_length=255)


class Site(BaseModel):
    key = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    owner = models.OneToOneField(KontentUser, related_name='site')


class ContentGroup(BaseModel):
    site = models.OneToOneField(Site)
    #filter = models.One
    parent = models.ManyToManyField('self', related_name='parent')


class ContentObject(BaseModel):
    site = models.OneToOneField(Site)

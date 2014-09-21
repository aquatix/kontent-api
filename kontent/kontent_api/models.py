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
    title = models.CharField(max_length=255)
    owner = models.OneToOneField(KontentUser, related_name='site')

    def __unicode__(self):
        return '{0} [{1}]'.format(self.title, self.key)


class ContentGroup(BaseModel):
    """
    Group of content items; can be used as 'category' for example
    """
    title = models.CharField(max_length=255)
    site = models.OneToOneField(Site)
    #filter = models.One
    parent = models.ManyToManyField('self', related_name='parent', blank=True)


class ContentObject(BaseModel):
    site = models.OneToOneField(Site)
    protected = models.BooleanField(default=False)

    class Meta:
        pass


class GenericItem(BaseModel):
    """
    Abstract content item with shared properties
    """
    site = models.OneToOneField(Site)
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract: True


class TextItem(GenericItem):
    """
    Content item like an article: centered around its body text
    """
    body = models.TextField(blank=True)
    external_link = models.CharField(max_length=255, blank=True)

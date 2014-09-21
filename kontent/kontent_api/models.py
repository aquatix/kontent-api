from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ('-date_created', )


class KontentUser(BaseModel):
    user = models.OneToOneField(User, related_name='authuser')
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return '{0} [{1}]'.format(self.name, self.user)


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


class Tag(BaseModel):
    tag = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='tag')

    def __unicode__(self):
        return '{0} [{1}]'.format(self.tag, self.slug)


class ContentObject(BaseModel):
    site = models.OneToOneField(Site)
    protected = models.BooleanField(default=False)


class ContentItem(BaseModel):
    """
    Content item like an article: centered around its body text
    """
    ARTICLE = 0
    LINK = 1
    SNIPPET = 2
    IMAGE = 3
    BINARY = 4
    CHOICES = (
            (ARTICLE, 'Article'),
            (LINK, 'Link'),
            (SNIPPET, 'Snippet'),
            (IMAGE, 'Image'),
            (BINARY, 'Attachment'),
    )

    contenttype = models.IntegerField(choices=CHOICES, default=ARTICLE)
    site = models.ForeignKey(Site, related_name='site')
    author = models.ForeignKey(KontentUser, related_name='author')
    title = models.CharField(max_length=255, blank=True)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    public = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    publish_from = models.DateTimeField(blank=True, null=True)
    publish_to = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)

    protected = models.BooleanField(default=False)
    #password = models.

    # Content item like an article: centered around its body text
    body = models.TextField(blank=True)

    # If linking to external source
    external_link = models.CharField(max_length=3000, blank=True)
    original_url = models.CharField(max_length=3000, blank=True) # For example a shorted uri

    # Image item
    image_width = models.IntegerField(default=0)
    image_height = models.IntegerField(default=0)
    image = models.ImageField(width_field=image_width, height_field=image_height, blank=True)

    def save(self, *args, **kwargs):
        #if not self.id and (original_url and not external_link):
        if self.original_url and not self.external_link:
            # Try to de-tiny-fy the url
            self.external_link = self.deredirect(self.original_url)

        super(ContentItem, self).save(*args, **kwargs)

    def deredirect(self, uri):
        """
        Try to get the original uri from a shortened/redirectified uri
        """
        import urllib2, httplib
        request = urllib2.Request(uri)
        opener = urllib2.build_opener()
        f = opener.open(request)
        return f.url

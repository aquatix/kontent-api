from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

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
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(test, self).save(*args, **kwargs)


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
    site = models.OneToOneField(Site)
    author = models.ForeignKey(KontentUser, related_name='author')
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(blank=True)
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
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(ContentItem, self).save(*args, **kwargs)

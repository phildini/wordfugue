from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.utils import timezone
from model_utils.models import TimeStampedModel


class PublishedPostManager(models.Manager):

    def get_queryset(self):
        return super(PublishedPostManager, self).get_queryset().filter(
            is_published=True,
            publish_date__lte=timezone.now(),
        )

class BlogPost(TimeStampedModel):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField()
    publish_date = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    published_posts = PublishedPostManager()

    def __str__(self):
        return "{} by {}".format(self.title, self.author)

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})

    def get_canonical_url(self):
        return "{}{}{}".format(
            settings.PROTOCOL,
            Site.objects.get_current().domain,
            self.get_absolute_url(),
        )

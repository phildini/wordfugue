from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from model_utils.models import TimeStampedModel


class BlogPost(TimeStampedModel):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField()
    publish_date = models.DateTimeField()

    def __str__(self):
        return "{} by {}".format(self.title, self.author)

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})
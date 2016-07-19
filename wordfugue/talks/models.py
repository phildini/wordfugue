from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from model_utils.models import TimeStampedModel
from blog.models import Tag


class Talk(TimeStampedModel):

    speaker = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    date = models.DateField(blank=True, null=True)
    sites = models.ManyToManyField(Site)
    tags = models.ManyToManyField(Tag, blank=True)

    def get_absolute_url(self):
        return reverse("talks:talk", kwargs={"slug": self.slug})

    def get_canonical_url(self):
        return "{}{}{}".format(
            settings.PROTOCOL,
            Site.objects.get_current().domain,
            self.get_absolute_url(),
        )
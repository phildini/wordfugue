from django.db import models
from django.contrib.sites.models import Site
from jsonfield import JSONField


class SiteSettings(models.Model):
    site = models.ForeignKey(Site)
    settings = JSONField()

    def __str__(self):
        return "{} settings".format(self.site)
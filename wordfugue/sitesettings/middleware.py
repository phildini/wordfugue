from django.conf import settings
from django.contrib.sites.models import Site
from .models import SiteSettings


class SiteSettingsMiddleware(object):

    def process_request(self, request):
        try:
            request.site = Site.objects._get_site_by_request(request)
            settings.SITE_ID = request.site.id
        except Site.DoesNotExist:
            request.site = None

        try:
            request.sitesettings = SiteSettings.objects.get(site=request.site)
        except SiteSettings.DoesNotExist:
            request.site_settings = None
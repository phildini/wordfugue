from django.conf import settings
from django.contrib.sites.models import Site
from .models import SiteSettings


class SiteSettingsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request.site = Site.objects._get_site_by_request(request)
            settings.SITE_ID = request.site.id
        except Site.DoesNotExist:
            request.site = None

        try:
            request.sitesettings = SiteSettings.objects.get(site=request.site)
        except SiteSettings.DoesNotExist:
            request.site_settings = None

        return self.get_response(request)
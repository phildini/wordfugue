from django.conf import settings
from django.contrib.sites.models import Site

from .models import SiteSettings


class SiteSettingsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request.wf_site = Site.objects._get_site_by_request(request)
            settings.SITE_ID = request.wf_site.id
        except Site.DoesNotExist:
            request.wf_site = None

        try:
            request.sitesettings = SiteSettings.objects.get(site=request.wf_site)
        except SiteSettings.DoesNotExist:
            request.sitesettings = None

        return self.get_response(request)

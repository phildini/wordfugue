from django.conf import settings
from django.contrib.sites.models import Site

class SetSiteMiddleware(object):

    def process_request(self, request):
        try:
            request.site = Site.objects._get_site_by_request(request)
            settings.SITE_ID = request.site.id
        except Site.DoesNotExist:
            request.site = None
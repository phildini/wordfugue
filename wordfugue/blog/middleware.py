from django.contrib.sites.models import Site

class SetSiteMiddleware(object):

    def process_request(self, request):
        try:
            request.site = Site.objects._get_site_by_request(request)
        except Site.DoesNotExist:
            request.site = None
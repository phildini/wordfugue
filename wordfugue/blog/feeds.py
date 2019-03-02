from django.contrib.syndication.views import Feed
from django.http import Http404

from .models import BlogPost


class BlogFeed(Feed):

    def get_feed(self, obj, request):
        self.site = request.wf_site
        if not self.site:
            raise Http404()
        return super(BlogFeed, self).get_feed(obj, request)

    def title(self):
        return self.site.name

    def link(self):
        return self.site.domain

    def feed_url(self):
        return "{}/feed/".format(self.site.domain)

    def description(self):
        return "The latest posts from {}".format(self.site.name)

    def items(self):
        return BlogPost.objects.get_published_posts_for_site(self.site).order_by(
            '-publish_date'
        )[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_pubdate(self, item):
        return item.publish_date

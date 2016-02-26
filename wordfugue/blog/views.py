from django.views.generic import DetailView
from . import models
from django.contrib.sites.shortcuts import get_current_site


class BlogPostView(DetailView):

    model = models.BlogPost
    template_name = 'blog/blog_post_page.html'

    def get_queryset(self):
        return models.BlogPost.objects.get_published_posts_for_site(
            self.request.site
        )

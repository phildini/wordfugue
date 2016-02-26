from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.sites.shortcuts import get_current_site

from blog.models import BlogPost


class HomeView(ListView):

    template_name = "home/home.html"
    model = BlogPost
    paginate_by = 10
    paginate_orphans = 3

    def get_queryset(self):
        return BlogPost.objects.get_published_posts_for_site(
            self.request.site
        )



from django.shortcuts import render
from django.views.generic import ListView

from blog.models import BlogPost


class HomeView(ListView):

    template_name = "home/home.html"
    model = BlogPost
    queryset = BlogPost.published_posts.all()
    paginate_by = 10
    paginate_orphans = 3



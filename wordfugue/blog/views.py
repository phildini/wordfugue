from django.views.generic import DetailView
from . import models


class BlogPostView(DetailView):

    model = models.BlogPost
    template_name = 'blog_post.html'

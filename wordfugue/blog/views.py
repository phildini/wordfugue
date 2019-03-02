from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from . import models


class BlogPostView(DetailView):

    model = models.BlogPost
    template_name = 'blog/blog_post_page.html'

    def get_queryset(self):
        return models.BlogPost.objects.get_published_posts_for_site(
            self.request.wf_site
        )


class BlogPostPreviewView(LoginRequiredMixin, StaffuserRequiredMixin, DetailView):

    model = models.BlogPost
    template_name = 'blog/blog_post_page.html'


class TaggedPostView(ListView):

    model = models.BlogPost
    template_name = "home/home.html"
    paginate_by = 10
    paginate_orphans = 3

    def dispatch(self, *args, **kwargs):
        self.tag = get_object_or_404(models.Tag, slug=self.kwargs.get('slug'))
        return super(TaggedPostView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return models.BlogPost.objects.get_published_posts_for_site(
            self.request.wf_site
        ).filter(tags__id=self.tag.id).order_by('-publish_date')

    def get_context_data(self, *args, **kwargs):
        context = super(TaggedPostView, self).get_context_data(*args, **kwargs)
        context['tag'] = self.tag
        return context

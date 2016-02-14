from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import BlogPost


class HomeView(TemplateView):

    template_name = "home/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['posts'] = BlogPost.objects.all().order_by('-publish_date')[:5]
        return context



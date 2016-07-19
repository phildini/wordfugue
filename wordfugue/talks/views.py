from django.views.generic import DetailView, ListView
from . import models
from django.contrib.sites.shortcuts import get_current_site

from django.shortcuts import (
    get_object_or_404,
    redirect,
)

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)


class TalkView(DetailView):

    model = models.Talk
    template_name = 'talks/talk.html'


class TalkListView(ListView):

    template_name = "talks/list.html"
    model = models.Talk
    paginate_by = 10
    paginate_orphans = 3

class TaggedTalkView(ListView):

    model = models.Talk
    template_name = "talks/list.html"
    paginate_by = 10
    paginate_orphans = 3

    def dispatch(self, *args, **kwargs):
        self.tag = get_object_or_404(models.Tag, slug=self.kwargs.get('slug'))
        return super(TaggedTalkView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return models.Talk.objects.filter(tags__id=self.tag.id).order_by('-date')

    def get_context_data(self, *args, **kwargs):
        context = super(TaggedTalkView, self).get_context_data(*args, **kwargs)
        context['tag'] = self.tag
        return context

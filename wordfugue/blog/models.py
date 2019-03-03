from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from model_utils.models import TimeStampedModel
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         MultiFieldPanel)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class BlogIndexPage(Page, TimeStampedModel):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro", classname="full")]

    def __str__(self):
        return f"Blog Index: {self.title}"

    def get_admin_display_title(self):
        return str(self)

    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)

        context["blog_entries"] = (
            BlogPage.objects.child_of(self).live().order_by("-date")
        )
        return context


class WordfugueHomePage(BlogIndexPage):
    def get_template(self, request):
        return "blog/blog_index_page.html"

    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        wf_blog_entries = context["blog_entries"]
        other_site_entries = BlogPage.objects.live().exclude(restrict_to_site=True)
        all_entries = wf_blog_entries | other_site_entries
        context["blog_entries"] = all_entries.order_by("-date")

        return context


class BlogTag(TaggedItemBase, TimeStampedModel):
    content_object = ParentalKey(
        "BlogPage", related_name="tagged_items", on_delete=models.CASCADE
    )


class BlogPage(Page, TimeStampedModel):
    date = models.DateTimeField("Post date")
    intro = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)
    disqus_identifier = models.CharField(
        help_text="This shouldn't need to be changed", blank=True, max_length=255
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    restrict_to_site = models.BooleanField("Restrict to original site", default=False)
    tags = ClusterTaggableManager(through=BlogTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("date"),
                FieldPanel("tags"),
                FieldPanel("author"),
                FieldPanel("restrict_to_site"),
            ],
            heading="Post Meta",
        ),
        FieldPanel("intro"),
        FieldPanel("body"),
        # InlinePanel("gallery_images", label="Gallery images"),
    ]

    def __str__(self):
        return f"Blog Post: {self.title}"

    def get_admin_display_title(self):
        return str(self)

    def get_disqus_id(self):
        if self.disqus_identifier:
            return self.disqus_identifier
        else:
            return self.slug


class BlogTagIndexPage(Page, TimeStampedModel):
    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get("tag")
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context["blogpages"] = blogpages
        return context


class Tag(TimeStampedModel):

    tag = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    sites = models.ManyToManyField(Site)

    def __str__(self):
        return self.tag


class PublishedPostForSiteManager(models.Manager):
    def get_published_posts_for_site(self, site):
        return (
            super(PublishedPostForSiteManager, self)
            .get_queryset()
            .filter(
                is_published=True, publish_date__lte=timezone.now(), sites__in=[site]
            )
        )


class BlogPost(TimeStampedModel):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=True
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField()
    publish_date = models.DateTimeField(blank=True, null=True)
    disqus_identifier = models.CharField(
        help_text="This shouldn't need to be changed", blank=True, max_length=255
    )
    sites = models.ManyToManyField(Site, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    objects = PublishedPostForSiteManager()

    def __str__(self):
        return "{} by {}".format(self.title, self.author)

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})

    def get_canonical_url(self):
        return "{}{}{}".format(
            settings.PROTOCOL,
            Site.objects.get_current().domain,
            self.get_absolute_url(),
        )

    def get_disqus_id(self):
        if self.disqus_identifier:
            return self.disqus_identifier
        else:
            return self.slug

    def description(self):
        return strip_tags(self.body)[:140]

from django.template.defaultfilters import title
from taggit.models import Tag

from .models import BlogIndexPage, BlogPage, BlogPost, BlogTag


def port_to_wagtail(nic_page_id, pjj_page_id, wf_page_id):
    nic_posts = [
        post
        for post in BlogPost.objects.all()
        if post.sites.filter(domain="www.oboechick.com")
    ]
    port_post_set(home_page_id=nic_page_id, post_set=nic_posts)

    pjj_posts = [
        post
        for post in BlogPost.objects.all()
        if post.sites.filter(domain="blog.philipjohnjames.com")
    ]
    port_post_set(home_page_id=pjj_page_id, post_set=pjj_posts)

    wf_posts = [
        post
        for post in BlogPost.objects.all()
        if post.sites.filter(domain="www.wordfugue.com")
        .exclude(domain="www.oboechick.com")
        .exclude(domain="blog.philipjohnjames.com")
    ]
    port_post_set(home_page_id=wf_page_id, post_set=wf_posts)


def port_post_set(home_page_id, post_set):
    home_page = BlogIndexPage.objects.get(id=home_page_id)

    for post in post_set:
        try:
            page = BlogPage.objects.get(title=post.title, slug=post.slug)
        except BlogPage.DoesNotExist:
            page = BlogPage()
            page.title = post.title
            page.slug = post.slug
            page.date = post.publish_date or post.created
            page.created = post.created
            page.modified = post.modified
            page.body = post.body
            page.disqus_identifier = post.disqus_identifier
            page.first_published_at = post.publish_date
            page.author = post.author

            for tag in post.tags.all():
                wag_tag, _ = Tag.objects.get_or_create(name=tag.tag)
                page.tags.add(wag_tag)

            home_page.add_child(instance=page)
            revision = page.save_revision(submitted_for_moderation=False)
            page.save()
            if post.is_published:
                revision.publish()

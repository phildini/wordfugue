from django.contrib import admin
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from suit_redactor.widgets import RedactorWidget

from .models import BlogPost, Tag

class BlogPostAdminForm(ModelForm):
    class Meta:
        widgets = {
            'body': CKEditorWidget
        }


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    view_on_site = True
    fieldsets = [
        ('Headline', {'fields': ('author', 'title')}),
        ('Body', {'classes': ('full-width',), 'fields': ('body',)}),
        ('Where/When', {'fields': ('is_published', 'publish_date', 'sites', 'tags')}),
        ('Advanced Options', {'fields': ('slug', 'disqus_identifier')})
    ]
    form = BlogPostAdminForm
    date_hierarchy = 'publish_date'
    list_display = ('title', 'author', 'publish_date', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'body')
    prepopulated_fields = {"slug": ("title",), "disqus_identifier": ("slug",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tag",)}

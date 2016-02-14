from django.contrib import admin
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget

from .models import BlogPost

class BlogPostAdminForm(ModelForm):
    class Meta:
        widgets = {
            'body': RedactorWidget(editor_options={'lang': 'en'})
        }

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    prepopulated_fields = {"slug": ("title",)}

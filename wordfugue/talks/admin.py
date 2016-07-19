from django.contrib import admin
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from suit_redactor.widgets import RedactorWidget

from .models import Talk

class TalkAdminForm(ModelForm):
    class Meta:
        widgets = {
            'body': CKEditorWidget
        }


@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    view_on_site = True
    fieldsets = [
        ('Headline', {'fields': ('speaker', 'title')}),
        ('Body', {'classes': ('full-width',), 'fields': ('body',)}),
        ('Where/When', {'fields': ('date', 'sites', 'tags')}),
        ('Advanced Options', {'fields': ('slug',)})
    ]
    form = TalkAdminForm
    list_display = ('title', 'speaker', 'date')
    search_fields = ('title', 'body')
    prepopulated_fields = {"slug": ("title",)}
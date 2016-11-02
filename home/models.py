from __future__ import absolute_import, unicode_literals

from django.db import models

from utils.translation import TranslatedField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page):

    title_es = models.CharField(max_length=255)

    body_en = RichTextField(null=True, blank=True)
    body_es = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('title_es'),
        FieldPanel('body_en'),
        FieldPanel('body_es'),
    ]

    translated_title = TranslatedField(
        'title',
        'title_es')
    body = TranslatedField(
        'body_en',
        'body_es')

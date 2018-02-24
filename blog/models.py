from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index
from wagtail.wagtailcore.blocks import StructBlock, TextBlock, ListBlock

class ImageCarouselBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(required=False)

    class Meta:
        icon = 'image'

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    intro_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    last_modified = models.DateField(
        "Date article modified", blank=True, auto_now=True
    )
    body = RichTextField(blank=True)
    slider = StreamField([
        ('image', ListBlock(ImageCarouselBlock(), icon="image")),
    ], blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    parent_page_types = ['home.HomePage']

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        ImageChooserPanel('intro_image'),
        FieldPanel('body', classname="full"),
        StreamFieldPanel('slider'),
    ]

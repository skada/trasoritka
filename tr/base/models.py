from django.db import models
from django.utils.functional import lazy
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, Collection
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.models import Image


class PageHeaderImage(Page):

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
    ]

    class Meta:
        abstract = True


COL_WIDTH_FULL = 12
COL_WIDTH_HALF = 6
COL_WIDTH_THIRD = 4
COL_WIDTH_QUARTER = 3

COL_WIDTHS = (
    (COL_WIDTH_FULL, _('Full width')),
    (COL_WIDTH_HALF, _('Half width')),
    (COL_WIDTH_THIRD, _('One third')),
    (COL_WIDTH_QUARTER, _('One quarter')),
)


class FullWidthImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    title = blocks.CharBlock(required=False)
    description = blocks.TextBlock(required=False)
    page = blocks.PageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)

    class Meta:
        template = 'blocks/full_width_image_block.html'


class RichTextColBlock(blocks.StructBlock):
    width = blocks.ChoiceBlock(COL_WIDTHS, COL_WIDTH_FULL, required=True)
    content = blocks.RichTextBlock(required=True)

    class Meta:
        template = 'blocks/rich_text_col_block.html'


class RichTextRowBlock(blocks.ListBlock):

    def __init__(self, *args, **kwargs):
        super(RichTextRowBlock, self).__init__(
            child_block=RichTextColBlock(),
            *args,
            **kwargs
        )

    class Meta:
        template = 'blocks/rich_text_row_block.html'


class HeaderBlock(blocks.StructBlock):
    header_type = blocks.IntegerBlock(required=True, min_value=1, max_value=6)
    header_text = blocks.CharBlock(required=True)

    class Meta:
        template = 'blocks/header_block.html'


class SectionBlock(blocks.StreamBlock):
    header = HeaderBlock()
    rows = RichTextRowBlock()

    class Meta:
        template = 'blocks/section_block.html'


class SeparatorBlock(blocks.StaticBlock):
    class Meta:
        template = 'blocks/separator_block.html'


class CarouselBlock(blocks.ListBlock):

    def __init__(self, *args, **kwargs):
        super(CarouselBlock, self).__init__(
            child_block=FullWidthImageBlock(),
            *args,
            **kwargs
        )
    class Meta:
        template = 'blocks/carousel_block.html'


class RichTextPage(Page):

    body = StreamField([
        ('full_size_image', FullWidthImageBlock()),
        ('section', SectionBlock()),
        ('separator', SeparatorBlock()),
        ('carousel', CarouselBlock()),
    ],
    blank=True,)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = _('Rich text Page')
        verbose_name_plural = _('Rich text Pages')
#
#
# class GalleryPage(PageHeaderImage):
#     collection = models.ForeignKey(Collection, null=True, blank=True, on_delete=models.SET_NULL)
#
#     content_panels = PageHeaderImage.content_panels + [
#         FieldPanel('collection'),
#     ]
#
#     def get_context(self, request, *args, **kwargs):
#         context = super(GalleryPage, self).get_context(request, *args, **kwargs)
#         if self.collection:
#             context['images'] = Image.objects.filter(collection=self.collection)
#         else:
#             context['images'] = None
#         return context
#
#     class Meta:
#         verbose_name = _('Gallery Page')
#         verbose_name_plural = _('Gallery Pages')

from django.db import models
from django.utils.functional import lazy
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, Collection
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
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


class ColBlock(blocks.StructBlock):
    width = blocks.ChoiceBlock(COL_WIDTHS, COL_WIDTH_FULL, required=True)


class LinkButtonBlock(ColBlock):
    title = blocks.CharBlock()
    page = blocks.PageChooserBlock(required=False)
    document = DocumentChooserBlock(required=False)

    class Meta:
        template = 'blocks/link_button_block.html'


class ColSliderBlock(ColBlock):
    images = blocks.StreamBlock([
        ('image', ImageChooserBlock())
    ])

    class Meta:
        template = 'blocks/col_slider_block.html'


class RichTextColBlock(ColBlock):
    content = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'blocks/rich_text_col_block.html'


class RichTextRawColBlock(ColBlock):
    content = blocks.RawHTMLBlock(required=False)

    class Meta:
        template = 'blocks/rich_text_col_block.html'


class RichTextColWithIconBlock(RichTextColBlock):
    icon = blocks.CharBlock()

    class Meta:
        template = 'blocks/rich_text_col_with_icon_block.html'


class AccordionItemBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    content = blocks.RichTextBlock(required=True)

    class Meta:
        template = 'blocks/accordion_item_block.html'


class AccordionBlock(ColBlock):

    accordion_items = blocks.StreamBlock([
        ('accordion_item', AccordionItemBlock())
    ])

    class Meta:
        template = 'blocks/accordion_block.html'


class AccordionWithTitleBlock(ColBlock):
    title = blocks.CharBlock()
    accordion_items = blocks.StreamBlock([
        ('accordion_item', AccordionItemBlock())
    ])

    class Meta:
        template = 'blocks/accordion_with_title_block.html'


class RichTextRowBlock(blocks.StreamBlock):
    accordion = AccordionBlock()
    accordion_with_title = AccordionWithTitleBlock()
    rich_text = RichTextColBlock()
    rich_text_raw = RichTextRawColBlock()
    rich_text_with_icon = RichTextColWithIconBlock()
    col_slider_block = ColSliderBlock()
    link_button = LinkButtonBlock()

    class Meta:
        template = 'blocks/rich_text_row_block.html'


class HeaderBlock(blocks.StructBlock):
    header_type = blocks.IntegerBlock(required=True, min_value=1, max_value=6)
    header_text = blocks.CharBlock(required=True)

    class Meta:
        template = 'blocks/header_block.html'


SECTION_PLAIN = 'empty'
SECTION_COLOR = 'bg-color'
SECTION_IMAGE = 'bg-image'
SECTION_TYPE = (
    (SECTION_PLAIN, _('Plain section')),
    (SECTION_COLOR, _('Color section')),
    (SECTION_IMAGE, _('Image section')),
)


class SectionBlock(blocks.StructBlock):
    section_type = blocks.ChoiceBlock(choices=SECTION_TYPE, default=SECTION_PLAIN)
    image = ImageChooserBlock(required=False)
    content = blocks.StreamBlock([
        ('header', HeaderBlock()),
        ('row', RichTextRowBlock()),
    ])

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


ICON_CHOICES = (
    ('im-user', _('User')),
    ('im-factory', _('Factory')),
    ('im-project', _('Project')),
    ('im-idea', _('Idea')),
)


class CounterItemBlock(blocks.StructBlock):
    width = blocks.ChoiceBlock(choices=COL_WIDTHS, default=COL_WIDTH_QUARTER)
    icon = blocks.ChoiceBlock(choices=ICON_CHOICES)
    count = blocks.IntegerBlock(min_value=0)
    label = blocks.CharBlock()


class CountersBlock(blocks.ListBlock):

    def __init__(self, *args, **kwargs):
        super(CountersBlock, self).__init__(
            child_block=CounterItemBlock(),
            *args,
            **kwargs
        )

    class Meta:
        template = 'blocks/counters_block.html'


class MiniSliderBlock(blocks.ListBlock):

    def __init__(self, *args, **kwargs):
        super(MiniSliderBlock, self).__init__(
            child_block=ImageChooserBlock(),
            *args,
            **kwargs
        )

    class Meta:
        template = 'blocks/minislider_block.html'


class ContactBlock(blocks.StructBlock):

    class Meta:
        template = 'blocks/contact_block.html'


class BigMapBlock(blocks.StructBlock):
    left_column = blocks.RawHTMLBlock(required=False)
    right_column = blocks.RawHTMLBlock(required=False)

    class Meta:
        template = 'blocks/big_map_block.html'


class RichTextPage(Page):

    body = StreamField([
        ('full_size_image', FullWidthImageBlock()),
        ('section', SectionBlock()),
        ('separator', SeparatorBlock()),
        ('carousel', CarouselBlock()),
        ('counters', CountersBlock()),
        ('minislider', MiniSliderBlock()),
        ('contact_panel', ContactBlock()),
    ],
    blank=True,)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = _('Rich text Page')
        verbose_name_plural = _('Rich text Pages')


class ContactPage(Page):
    body = StreamField([
        ('big_map', BigMapBlock()),
        ('section', SectionBlock()),
    ],
    blank=True,)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = _('Contact Page')
        verbose_name_plural = _('Contact Pages')

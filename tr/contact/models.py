from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.wagtailcore.blocks import PageChooserBlock
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField


class ContactFormField(AbstractFormField):
    page = ParentalKey('ContactForm', related_name='form_fields')


class ContactForm(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


class ContactFormChooserBlock(PageChooserBlock):
    
    def __init__(self, *args, **kwargs):
        super(ContactFormChooserBlock, self).__init__(
            target_model='contact.ContactForm',
            template='block/contact_form_block.html',
            *args, **kwargs
        )

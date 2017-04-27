# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tr.base.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_auto_20170418_2019'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField((('big_map', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('right_column', wagtail.wagtailcore.blocks.RawHTMLBlock())))), ('section', wagtail.wagtailcore.blocks.StructBlock((('section_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('empty', 'Plain section'), ('bg-color', 'Color section'), ('bg-image', 'Image section')])), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('content', wagtail.wagtailcore.blocks.StreamBlock((('header', wagtail.wagtailcore.blocks.StructBlock((('header_type', wagtail.wagtailcore.blocks.IntegerBlock(max_value=6, min_value=1, required=True)), ('header_text', wagtail.wagtailcore.blocks.CharBlock(required=True))))), ('row', wagtail.wagtailcore.blocks.StreamBlock((('accordion', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(12, 'Full width'), (6, 'Half width'), (4, 'One third'), (3, 'One quarter')])), ('accordion_items', wagtail.wagtailcore.blocks.StreamBlock((('accordion_item', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))),)))))), ('accordion_with_title', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(12, 'Full width'), (6, 'Half width'), (4, 'One third'), (3, 'One quarter')])), ('title', wagtail.wagtailcore.blocks.CharBlock()), ('accordion_items', wagtail.wagtailcore.blocks.StreamBlock((('accordion_item', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))),)))))), ('rich_text', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(12, 'Full width'), (6, 'Half width'), (4, 'One third'), (3, 'One quarter')])), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False))))), ('rich_text_raw', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(12, 'Full width'), (6, 'Half width'), (4, 'One third'), (3, 'One quarter')])), ('content', wagtail.wagtailcore.blocks.RawHTMLBlock(required=False))))), ('rich_text_with_icon', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(12, 'Full width'), (6, 'Half width'), (4, 'One third'), (3, 'One quarter')])), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock())))), ('col_slider_block', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(12, 'Full width'), (6, 'Half width'), (4, 'One third'), (3, 'One quarter')])), ('images', wagtail.wagtailcore.blocks.StreamBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),)))))))))))))))), blank=True)),
            ],
            options={
                'verbose_name': 'Contact Page',
                'verbose_name_plural': 'Contact Pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='richtextpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('full_size_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('description', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))), ('section', wagtail.wagtailcore.blocks.StructBlock((('section_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('empty', 'Plain section'), ('bg-color', 'Color section'), ('bg-image', 'Image section')])), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('content', wagtail.wagtailcore.blocks.StreamBlock((('header', wagtail.wagtailcore.blocks.StructBlock((('header_type', wagtail.wagtailcore.blocks.IntegerBlock(max_value=6, min_value=1, required=True)), ('header_text', wagtail.wagtailcore.blocks.CharBlock(required=True))))), ('row', wagtail.wagtailcore.blocks.StreamBlock((('accordion', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(12, 'Full width'), (6, 'Half width'), (4, 'One third'), (3, 'One quarter')])), ('accordion_items', wagtail.wagtailcore.blocks.StreamBlock((('accordion_item', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))),)))))), ('accordion_with_title', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(12, 'Full width'), (6, 'Half width'), (4, 'One third'), (3, 'One quarter')])), ('title', wagtail.wagtailcore.blocks.CharBlock()), ('accordion_items', wagtail.wagtailcore.blocks.StreamBlock((('accordion_item', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))),)))))), ('rich_text', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(12, 'Full width'), (6, 'Half width'), (4, 'One third'), (3, 'One quarter')])), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False))))), ('rich_text_raw', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(12, 'Full width'), (6, 'Half width'), (4, 'One third'), (3, 'One quarter')])), ('content', wagtail.wagtailcore.blocks.RawHTMLBlock(required=False))))), ('rich_text_with_icon', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(12, 'Full width'), (6, 'Half width'), (4, 'One third'), (3, 'One quarter')])), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock())))), ('col_slider_block', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(12, 'Full width'), (6, 'Half width'), (4, 'One third'), (3, 'One quarter')])), ('images', wagtail.wagtailcore.blocks.StreamBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),))))))))))))))), ('separator', tr.base.models.SeparatorBlock()), ('carousel', tr.base.models.CarouselBlock()), ('counters', tr.base.models.CountersBlock()), ('minislider', tr.base.models.MiniSliderBlock()), ('contact_panel', wagtail.wagtailcore.blocks.StructBlock(()))), blank=True),
        ),
    ]
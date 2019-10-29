# Generated by Django 2.2.1 on 2019-10-25 20:19

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191025_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniontimeline',
            name='events',
            field=wagtail.core.fields.StreamField([('event', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.RichTextBlock(default='', required=True)), ('date', wagtail.core.blocks.RichTextBlock(default='', required=True)), ('body', wagtail.core.blocks.RichTextBlock(default='', required=True)), ('featured_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock(features=['italic'], required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text='Width of image in article.'))]))]))]),
        ),
    ]

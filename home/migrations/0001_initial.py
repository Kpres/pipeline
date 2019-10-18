# Generated by Django 2.2.1 on 2019-10-15 20:21

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('featured_articles', wagtail.core.fields.StreamField([('one_column', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.StructBlock([('article', wagtail.core.blocks.PageChooserBlock(page_type=['core.ArticlePage'])), ('headline', wagtail.core.blocks.RichTextBlock(help_text="Optional. Will override the article's headline.", required=False))]))])), ('one_ad_column', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image should be 22:7')), ('link', wagtail.core.blocks.URLBlock(label='target', required=False))])), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StructBlock([('article', wagtail.core.blocks.PageChooserBlock(page_type=['core.ArticlePage'])), ('headline', wagtail.core.blocks.RichTextBlock(help_text="Optional. Will override the article's headline.", required=False))])), ('right_column', wagtail.core.blocks.StructBlock([('article', wagtail.core.blocks.PageChooserBlock(page_type=['core.ArticlePage'])), ('headline', wagtail.core.blocks.RichTextBlock(help_text="Optional. Will override the article's headline.", required=False))])), ('emphasize_column', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], help_text='Which article, if either, should appear larger.', required=False))])), ('three_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StructBlock([('article', wagtail.core.blocks.PageChooserBlock(page_type=['core.ArticlePage'])), ('headline', wagtail.core.blocks.RichTextBlock(help_text="Optional. Will override the article's headline.", required=False))])), ('middle_column', wagtail.core.blocks.StructBlock([('article', wagtail.core.blocks.PageChooserBlock(page_type=['core.ArticlePage'])), ('headline', wagtail.core.blocks.RichTextBlock(help_text="Optional. Will override the article's headline.", required=False))])), ('right_column', wagtail.core.blocks.StructBlock([('article', wagtail.core.blocks.PageChooserBlock(page_type=['core.ArticlePage'])), ('headline', wagtail.core.blocks.RichTextBlock(help_text="Optional. Will override the article's headline.", required=False))]))])), ('recent_articles', wagtail.core.blocks.StructBlock([('num_articles', wagtail.core.blocks.IntegerBlock(help_text='Number of recent articles to display.', label='Number of articles'))])), ('marquee_banner', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True)), ('banner_type', wagtail.core.blocks.ChoiceBlock(choices=[('moves', 'Rotating')], help_text='Determines whether the marquee banner is stationary or rotating. Only rotating works right now.'))]))], null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]

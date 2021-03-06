# Generated by Django 2.2 on 2019-04-29 18:07

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [("core", "0007_auto_20190429_1739")]

    operations = [
        migrations.AlterField(
            model_name="articlepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    ("paragraph", wagtail.core.blocks.RichTextBlock()),
                    (
                        "photo",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("caption", wagtail.core.blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                    (
                        "photo_gallery",
                        wagtail.core.blocks.ListBlock(
                            wagtail.snippets.blocks.SnippetChooserBlock("core.Photo"),
                            icon="image",
                        ),
                    ),
                    (
                        "embed",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "embed",
                                    wagtail.embeds.blocks.EmbedBlock(
                                        help_text="URL to the content to embed."
                                    ),
                                )
                            ]
                        ),
                    ),
                ]
            ),
        )
    ]

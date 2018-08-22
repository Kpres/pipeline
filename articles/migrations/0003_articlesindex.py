# Generated by Django 2.0.7 on 2018-07-12 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0040_page_draft_title"),
        ("articles", "0002_articlepage_headline"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticlesIndex",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                )
            ],
            options={"abstract": False},
            bases=("wagtailcore.page",),
        )
    ]

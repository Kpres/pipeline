# Generated by Django 2.0.8 on 2018-08-17 23:24

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [("core", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="staticpage",
            name="body",
            field=wagtail.core.fields.RichTextField(default=""),
            preserve_default=False,
        )
    ]

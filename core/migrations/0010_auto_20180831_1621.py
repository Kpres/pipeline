# Generated by Django 2.0.8 on 2018-08-31 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("core", "0009_photo")]

    operations = [
        migrations.RenameField(model_name="photo", old_name="photo", new_name="image")
    ]
# Generated by Django 2.2.9 on 2020-01-31 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_candidatepage_nominations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatepage',
            name='offices',
        ),
    ]

# Generated by Django 2.2.9 on 2020-01-31 00:18

from django.db import migrations, models
import wagtail.core.fields
import wagtail.search.index


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_electionindexpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rcs_id', models.CharField(max_length=255)),
                ('rich_name', wagtail.core.fields.RichTextField(blank=True, max_length=255, null=True)),
                ('nominations', models.IntegerField()),
                ('bio', wagtail.core.fields.RichTextField(blank=True, max_length=3000, null=True)),
            ],
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]

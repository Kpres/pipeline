# Generated by Django 2.0.7 on 2018-07-17 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articlesindex'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='featured_article',
            field=models.ForeignKey(blank=True, help_text='Article that is displayed prominently at the top of the home page.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.ArticlePage'),
        ),
    ]
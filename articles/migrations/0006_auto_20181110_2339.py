# Generated by Django 2.0.9 on 2018-11-10 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("articles", "0005_migrationinformation")]

    operations = [
        migrations.RemoveField(model_name="migrationinformation", name="id"),
        migrations.AlterField(
            model_name="migrationinformation",
            name="guid",
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 3.0.3 on 2020-05-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0005_remove_foods_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
# Generated by Django 3.0.3 on 2020-05-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
        ('Restaurants', '0009_restaurants_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurants',
            name='category',
        ),
        migrations.AddField(
            model_name='restaurants',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='restaurant', to='Category.Category'),
        ),
    ]

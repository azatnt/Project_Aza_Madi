# Generated by Django 3.0.3 on 2020-05-31 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurants', '0018_foods_food_category'),
        ('Category', '0006_remove_food_category_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_category',
            name='restaurant',
            field=models.ManyToManyField(blank=True, related_name='restaurant', to='Restaurants.Restaurants'),
        ),
    ]
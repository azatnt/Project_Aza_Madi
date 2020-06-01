# Generated by Django 3.0.3 on 2020-05-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0004_food_category'),
        ('Restaurants', '0013_foods_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foods',
            name='category',
        ),
        migrations.AddField(
            model_name='foods',
            name='food_category',
            field=models.ManyToManyField(blank=True, related_name='food', to='Category.Food_Category'),
        ),
    ]
# Generated by Django 3.0.3 on 2020-05-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurants', '0005_auto_20200507_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='image',
            field=models.ImageField(blank=True, default='smth', upload_to='rest-image'),
        ),
    ]

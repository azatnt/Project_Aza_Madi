# Generated by Django 3.0.3 on 2020-05-09 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
        ('Restaurants', '0008_auto_20200508_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Category.Category'),
        ),
    ]

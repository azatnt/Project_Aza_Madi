# Generated by Django 3.0.3 on 2020-06-08 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_useraddress_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='user',
        ),
    ]
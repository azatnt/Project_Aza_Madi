# Generated by Django 3.0.3 on 2020-06-08 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_remove_useraddress_user'),
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='User.UserAddress'),
        ),
    ]
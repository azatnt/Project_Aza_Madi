# Generated by Django 3.0.6 on 2020-05-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('surname', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, default='smth', upload_to='courier-image')),
            ],
        ),
    ]

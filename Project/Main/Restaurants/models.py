from django.db import models
from django.utils.text import slugify
from time import time
from Category.models import *




def gen_slug(s):
    new_slug = slugify(s)
    return new_slug + '-' + str(int(time()))




class Restaurants(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    image = models.ImageField(upload_to='rest-image', blank=True, default='smth')
    description = models.TextField(max_length=1000)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=50, unique=True)
    opening_time = models.CharField(max_length=120)
    average_delivery = models.CharField(max_length=120)
    category = models.ManyToManyField('Category.Category', blank=True, related_name='restaurant')


    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)




class Foods(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    image = models.ImageField(blank=True, upload_to='food-image', default='smth')
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    restaurant = models.ManyToManyField('Restaurants', related_name='food')


    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

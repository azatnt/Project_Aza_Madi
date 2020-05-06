from django.db import models
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s)
    return new_slug + '-' + str(int(time()))




class Restaurants(models.Model):
    name = models.CharField(max_length=120, unique=True) #name of restaurant
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='book-image', blank=True, default='smth')
    description = models.TextField(max_length=1000) #main information about restaurant
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=50, unique=True)
    opening_time = models.CharField(max_length=120) #for example: Monday-Sunday 10:00-20:00
    average_delivery = models.CharField(max_length=120) #for example: 20-30 min


    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

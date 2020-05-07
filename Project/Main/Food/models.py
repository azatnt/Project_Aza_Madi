from django.db import models
# from Restaurants.models import Restaurants
from django.utils.text import slugify
from time import time



# def gen_slug(s):
#     new_slug = slugify(s)
#     return new_slug + '-' + str(int(time()))
#
#
# class Foods(models.Model):
#     name = models.CharField(max_length=120)
#     slug = models.SlugField(blank=True)
#     image = models.ImageField(blank=True)
#     price = models.IntegerField()
#     description = models.TextField(max_length=1000)
#
#
#     def __str__(self):
#         return str(self.name)
#
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.slug = gen_slug(self.name)
#         super().save(*args, **kwargs)

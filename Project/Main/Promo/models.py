from django.db import models
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s)
    return new_slug + '-' + str(int(time()))


class Promo(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='promo-image', blank=True)
    description = models.CharField(max_length=120)


    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

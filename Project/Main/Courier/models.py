from django.db import models





class Courier(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    image = models.ImageField(upload_to='courier-image', blank=True, default='smth')


    def __str__(self):
        return str(self.name)

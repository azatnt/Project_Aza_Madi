from django.db import models
from django.contrib.auth.models import User





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user-profile-image', blank=True, default='default.jpeg')
    back_image = models.ImageField(upload_to='user-profile-image', blank=True, default='def_back.jpg')



    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

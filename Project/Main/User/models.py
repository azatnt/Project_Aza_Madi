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




class UserAddress(models.Model):
	address = models.CharField(max_length=120)
	address2 = models.CharField(max_length=120, null=True, blank=True)
	postcode = models.CharField(max_length=90)
	phone = models.CharField(max_length=30)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return str(self.user.username)

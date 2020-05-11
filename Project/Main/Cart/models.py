from django.db import models
from Restaurants.models import *


class Cart(models.Model):
    total = models.DecimalField(default=0, max_digits=1000, decimal_places=0)
    imestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return 'Cart ID: %s' %(self.id)



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Foods, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    line_total = models.DecimalField(default=0, max_digits=1000, decimal_places=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title

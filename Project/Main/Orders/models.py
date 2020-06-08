from django.db import models
from Cart.models import Cart
from django.contrib.auth import get_user_model
from User.models import UserAddress


User = get_user_model()

STATUS_CHOICES = (
    ('Started', 'Started'),
    ('Abandoned', 'Abandoned'),
    ('Ready', 'Ready'),
    ('Courier Taking', 'Courier Taking'),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    order_id = models.CharField(max_length=150, default='98JGHE', unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    final_total = models.DecimalField(default=0, max_digits=1000, decimal_places=1)

    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default='Started')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id

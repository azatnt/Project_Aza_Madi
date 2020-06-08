from django.shortcuts import render
from Orders.models import *
from User.models import *





def courier(request):
    orders = Order.objects.all()
    return render(request, 'courier/order_list.html', context={'orders':orders, 'user': user})

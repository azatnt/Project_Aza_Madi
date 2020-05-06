from django.shortcuts import render
from .models import *




def restaurant_list(request):
    restaurant = Restaurants.objects.all()
    return render(request, 'restaurants/restaurants_list.html', context={'restaurant': restaurant})

from django.shortcuts import render
from .models import *
from Promo.models import *
from Category.models import *




def restaurant_list(request):
    restaurant = Restaurants.objects.all()
    promo = Promo.objects.all()
    category = Category.objects.all()
    context = {
        'category':category,
        'restaurant': restaurant,
        'promo':promo
    }
    return render(request, 'restaurants/restaurants_list.html', context=context)

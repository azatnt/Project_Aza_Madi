from django.shortcuts import render
from .models import *
from Promo.models import *
from Category.models import *




def restaurant_list(request):
    restaurant = Restaurants.objects.all()
    promo = Promo.objects.all()
    category = Category.objects.all()
    context = {
        'restaurant': restaurant,
        'category':category,
        'promo':promo
    }
    return render(request, 'restaurants/restaurants_list.html', context=context)


# def rest_name(request, name):
#     rest_name = Restaurants.objects.filter(name=name)
#     return render(request, 'restaurants/rest_name.html', context={'rest_name':rest_name})

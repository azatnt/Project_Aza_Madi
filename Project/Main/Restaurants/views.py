from django.shortcuts import render
from .models import *
from Promo.models import *
from Category.models import *




def search_field(request):
    if request.method == 'POST':
        search = request.POST['search']
    else:
        search = ''
    restaurants = Restaurants.objects.filter(name__icontains=search)
    return render(request, 'restaurants/search.html', context={'restaurants':restaurants})



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

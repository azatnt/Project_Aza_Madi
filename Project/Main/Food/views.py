from django.shortcuts import render
from .models import *
from Restaurants.models import *



def food_list(request):
    food = Foods.objects.all()
    return render(request, 'food/food_list.html', context={'food':food})

from django.shortcuts import render
from Restaurants.models import *



def index(request):
	return render(request, 'Miri/index.html', context={})



def restaurant_detail(request, slug):
	restaurant = Restaurants.objects.get(slug__exact=slug)
	food = Foods.objects.all()
	context = {
		'food':food,
		'restaurant':restaurant
	}
	return render(request, 'Miri/restaurant_detail.html', context=context)

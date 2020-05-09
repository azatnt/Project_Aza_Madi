from django.shortcuts import render
from Restaurants.models import *
from Category.models import *



def index(request):
	return render(request, 'Miri/index.html', context={})



def restaurant_detail(request, slug):
	restaurant = Restaurants.objects.get(slug__iexact=slug)
	food = Foods.objects.all()
	context = {
		'food':food,
		'restaurant':restaurant
	}
	return render(request, 'Miri/restaurant_detail.html', context=context)



def category_detail(request, slug):
	category = Category.objects.get(slug__iexact=slug)
	return render(request, 'Miri/category_detail.html', context={'category':category})

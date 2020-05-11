from django.shortcuts import render, get_object_or_404
from Restaurants.models import *
from Category.models import *





def restaurant_detail(request, slug):
	restaurant = Restaurants.objects.get(slug__iexact=slug)
	food = Foods.objects.all()
	return render(request, 'Miri/restaurant_detail.html', context={'food':food, 'restaurant':restaurant})






def category_detail(request, slug):
	category = Category.objects.get(slug__iexact=slug)
	return render(request, 'Miri/category_detail.html', context={'category':category})

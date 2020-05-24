from django.shortcuts import render, HttpResponse
from Restaurants.models import *
from Category.models import *




def restaurant_detail(request, slug):
	restaurant = Restaurants.objects.get(slug__iexact=slug)
	rest_name = Restaurants.objects.filter(slug=slug)
	food = Foods.objects.all()
	template = 'Miri/restaurant_detail.html'
	context = {
		'food':food,
		'restaurant':restaurant,
		'rest_name':rest_name
	}
	return render(request, template, context)




def category_detail(request, slug):
	category = Category.objects.get(slug__iexact=slug)
	template = 'Miri/category_detail.html'
	context = {
		'category':category
	}
	return render(request, template, context)

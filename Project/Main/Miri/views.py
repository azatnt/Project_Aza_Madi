from django.shortcuts import render, HttpResponse
from Restaurants.models import *
from Category.models import *
from django.views.generic import View
from django.shortcuts import get_object_or_404




class RestaurantDetail(View):
	def get(self, request, slug):
		restaurant = get_object_or_404(Restaurants, slug__iexact=slug)
		rest_name = get_object_or_404(Restaurants, slug=slug)
		rest_name = Restaurants.objects.filter(slug=slug)
		food = Foods.objects.all()
		template = 'Miri/restaurant_detail.html'
		context = {
			'food':food,
			'restaurant':restaurant,
			'rest_name':rest_name
		}
		return render(request, template, context)




class CategoryDetail(View):
	def get(self, request, slug):
		category = get_object_or_404(Category, slug__iexact=slug)
		template = 'Miri/category_detail.html'
		context = {
			'category':category
		}
		return render(request, template, context)

from django.shortcuts import render, HttpResponse
from Restaurants.models import *
from Category.models import *
from django.views.generic import View, ListView
from django.shortcuts import get_object_or_404




class RestaurantDetail(View):
	model1 = Restaurants
	model2 = Foods
	template = 'Miri/restaurant_detail.html'

	def get(self, request, slug):
		restaurant = get_object_or_404(Restaurants, slug__iexact=slug)
		rest_name = get_object_or_404(Restaurants, slug=slug)
		rest_name = self.model1.objects.filter(slug=slug)
		food = self.model2.objects.all()

		context = {
			'food':food,
			'restaurant':restaurant,
			'rest_name':rest_name
		}
		return render(request, self.template, context)




class CategoryDetail(View):
	template = 'Miri/category_detail.html'

	def get(self, request, slug):
		category = get_object_or_404(Category, slug__iexact=slug)
		context = {
			'category':category
		}
		return render(request, self.template, context)

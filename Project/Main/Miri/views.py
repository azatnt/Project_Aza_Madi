from django.shortcuts import render, HttpResponse
from Restaurants.models import *
from Category.models import *
from django.views.generic import View, ListView
from django.shortcuts import get_object_or_404




class RestaurantDetail(View):
	model1 = Restaurants
	model2 = Foods
	model3 = Food_Category
	template = 'Miri/restaurant_detail.html'

	def get(self, request, slug):
		restaurant = get_object_or_404(Restaurants, slug__iexact=slug)
		rest_name = get_object_or_404(Restaurants, slug=slug)
		rest_name = self.model1.objects.filter(slug=slug)
		food = self.model2.objects.all()
		rest_category = self.model3.objects.all()
		context = {
			'food':food,
			'restaurant':restaurant,
			'rest_name':rest_name,
			'rest_category':rest_category
		}
		return render(request, self.template, context)


def food_category(request, slug, rest_slug):
	# rest_id = get_object_or_404(Restaurants, slug=rest_slug)
	rest_id = Restaurants.objects.filter(slug=rest_slug)
	food = get_object_or_404(Food_Category, slug=slug)
	context = {
			'food':food,
			'rest_id':rest_id
			}
	return render(request, 'Miri/food_category.html', context)


class CategoryDetail(View):
	template = 'Miri/category_detail.html'

	def get(self, request, slug):
		category = get_object_or_404(Category, slug__iexact=slug)
		context = {
			'category':category
		}
		return render(request, self.template, context)

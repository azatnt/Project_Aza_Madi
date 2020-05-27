from django.shortcuts import render
from .models import *
from Promo.models import *
from Category.models import *
from django.views.generic import View, ListView



class SearchField(View):
    model = Restaurants
    template = 'restaurants/search.html'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            search = request.POST['search']
        else:
            search = ''
        restaurants = self.model.objects.filter(name__icontains=search)
        context = {
            'restaurants':restaurants
        }
        return render(request, self.template, context)




class RestaurantsList(View):
    model1 = Restaurants
    model2 = Promo
    model3 = Category
    template = 'restaurants/restaurants_list.html'
    def get(self, request, *args, **kwargs):
        restaurant = self.model1.objects.all()
        promo = self.model2.objects.all()
        category = self.model3.objects.all()
        context = {
            'restaurant': restaurant,
            'category':category,
            'promo':promo
        }
        return render(request, self.template, context)

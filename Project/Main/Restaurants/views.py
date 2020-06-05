from django.shortcuts import render
from .models import *
from Promo.models import *
from Category.models import *
from django.views.generic import View, ListView
from django.core.paginator import Paginator




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
        paginator = Paginator(restaurant, 2)

        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''

        context = {
            'page_object': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url,
            'category':category,
            'promo':promo
        }
        return render(request, self.template, context)

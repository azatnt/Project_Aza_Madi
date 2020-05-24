from django.shortcuts import render
from .models import *
from Promo.models import *
from Category.models import *




def restaurant_list(request):
    restaurant = Restaurants.objects.all()
    promo = Promo.objects.all()
    category = Category.objects.all()
    context = {
        'restaurant': restaurant,
        'category':category,
        'promo':promo
    }
    return render(request, 'restaurants/restaurants_list.html', context=context)




def search(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''
	restaurants = Restaurants.objects.filter(name__icontains=search_text)
	return render(request, 'restaurants/ajax_search.html', {'restaurants':restaurants})

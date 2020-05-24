from django.shortcuts import render, HttpResponse
from Restaurants.models import *
from Category.models import *
from Cart.models import *
import json




# def test(request):
# 	cartitem = CartItem.objects.get(product=product)
# 	return render(request, 'Miri/test.html', context={'cartitem':cartitem})


# def search_auto(request):
#   if request.is_ajax():
#     q = request.GET.get('term', '')
#     restaurants = Place.objects.filter(name__icontains=q)
#     results = []
#     for rs in restaurants:
#       restaurant_json = {}
#       restaurant_json = rs.name
#       results.append(restaurant_json)
#     data = json.dumps(results)
#   else:
#     data = 'fail'
#   mimetype = 'application/json'
#   return HttpResponse(data, mimetype)

# def search(request):
# 	if request.method == 'POST':
# 		search_text = request.POST['search_text']
# 	else:
# 		search_text = ''
#
# 	restaurants = Restaurants.objects.filter(name__icontains=search_text)
# 	return render(request, 'Miri/ajax_search.html', {'restaurants':restaurants})




def restaurant_detail(request, slug):
	restaurant = Restaurants.objects.get(slug__iexact=slug)
	rest_name = Restaurants.objects.filter(slug=slug)
	food = Foods.objects.all()
	return render(request, 'Miri/restaurant_detail.html', context={'food':food,
																	'restaurant':restaurant,
																	'rest_name':rest_name})






def category_detail(request, slug):
	category = Category.objects.get(slug__iexact=slug)
	return render(request, 'Miri/category_detail.html', context={'category':category})

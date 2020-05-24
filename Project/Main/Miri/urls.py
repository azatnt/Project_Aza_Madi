from django.urls import path
from .views import *
from Restaurants.views import *
from Promo.views import *
from Category.views import *
from Cart.views import *
from User.views import *




urlpatterns = [
	path('', restaurant_list, name='restaurant_list_url'),
	path('<str:slug>', restaurant_detail, name='restaurant_detail_url'),
	path('profile/', profile, name='profile_url'),
	path('category/<slug:slug>', category_detail, name='category_detail_url'),
	path('cart/<str:id>\d+', remove_from_cart, name = 'remove_cart_url'),
	path('cart/<str:slug>/', update_cart, name = 'update_cart_url'),
	path('cart/', cart, name='cart_url'),
	path('search/', search, name='search_url'),
]

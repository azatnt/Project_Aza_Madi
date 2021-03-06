from django.urls import path
from .views import *
from Restaurants.views import *
from Promo.views import *
from Category.views import *
from Cart.views import *
from User.views import *
from Chat.views import *
from Orders.views import *
from Courier.views import *






urlpatterns = [
	path('', RestaurantsList.as_view(), name='restaurant_list_url'),
	path('<str:slug>', RestaurantDetail.as_view(), name='restaurant_detail_url'),
	path('category/<slug:slug>', CategoryDetail.as_view(), name='category_detail_url'),
	path('cart/<str:id>\d+', RemoveFromCart.as_view(), name = 'remove_cart_url'),
	path('cart/<str:slug>/', update_cart, name = 'update_cart_url'),
	path('cart/', cart, name='cart_url'),
	path('profile/', UserProfile.as_view(), name='profile_url'),
	path('category_food/<slug:slug>/<str:rest_slug>', food_category, name='food_category_detail_url'),
	path('search/', SearchField.as_view(), name='search_url'),
	path('chat/', index, name='index'),
	path('chat/<str:room_name>/', room, name='chat'),
	path('checkout/', checkout, name = 'checkout_url'),
	path('courier/', courier, name='courier_url'),

]

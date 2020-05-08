from django.conf.urls import url
from django.urls import path
from .views import *
from Restaurants.views import *
from Food.views import *
from Promo.views import *


urlpatterns = [
	path('', restaurant_list, name='restaurant_list_url'),
	path('restaurant/<str:slug>', restaurant_detail, name='restaurant_detail_url'),



]

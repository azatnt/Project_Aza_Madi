from django.conf.urls import url
from django.urls import path
from .views import *
from Restaurants.views import *


urlpatterns = [
	path('', restaurant_list, name='restaurant_list_url'),

]

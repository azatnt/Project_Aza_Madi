from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
	path('', index, name='index_urls'),
]
from Api.views import *
from django.urls import path

urlpatterns = [
    path('restaurants/', RestaurantsList.as_view(), name="restaurants_list_url"),
    path('restaurants/<str:slug>/', RestaurantDetail.as_view(), name="restaurants_detail_url"),
    path('category/', CategoryList.as_view(), name="category_list_url"),
    path('category/<str:slug>/', CategoryDetail.as_view(), name="category_detail_url"),
    path('foods/', FoodList.as_view(), name="food_list_url"),
]

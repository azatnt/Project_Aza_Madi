from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Restaurants.models import *
from Api.serializers import *
from rest_framework.views import APIView





class RestaurantsList(APIView):
    #list of all restaurant
    def get(self, request):
        restaurants = Restaurants.objects.all()
        serializer = RestaurantsListSerializer(restaurants, many = True)
        return Response(serializer.data)




class RestaurantDetail(APIView):
    #look into the restaurant
    def get(self, request, slug):
        try:
            restaurant = Restaurants.objects.get(slug = slug)
            serializer = RestaurantsDetailSerializer(restaurant)
            # serializer = serializers.TemperatureSerializer(data=request.data, context={'request': request})
            return Response(serializer.data)
        except Restaurants.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)


class CategoryList(APIView):
    #list of all category
    def get(self, request):
        try:
            category = Category.objects.all()
            serializer = CategoryListSerializer(category, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)


class CategoryDetail(APIView):
    #list of foods by category
    def get(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
            serializer = CategoryDetailSerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)


class FoodList(APIView):
    #list of all restaurant
    def get(self, request):
        foods = Foods.objects.all()
        serializer = FoodListSerializer(foods, many=True)
        return Response(serializer.data)


# class CreateFood(APIView):
#     #create food
#     def post(self, request):
#         serializer = FoodCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=201, serializer.data)
#         else:
#             return Response(status=400)

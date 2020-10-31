from rest_framework import serializers
from Restaurants.models import *



class RestaurantsListSerializer(serializers.ModelSerializer):
    #list of all restaurants

    class Meta:
        model = Restaurants
        fields = ('id', 'name', 'slug', 'phone')


class RestaurantsDetailSerializer(serializers.ModelSerializer):
    #resturant detail
    category = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)
    food = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)
    class Meta:
        model = Restaurants
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    #list of all category
    class Meta:
        model = Category
        fields = '__all__'

class CategoryDetailSerializer(serializers.ModelSerializer):
    #category detail
    restaurant = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    class Meta:
        model = Category
        fields = '__all__'


class FoodListSerializer(serializers.ModelSerializer):
    #List of all Foods
    restaurant = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)
    food_category = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)
    class Meta:
        model = Foods
        fields = '__all__'

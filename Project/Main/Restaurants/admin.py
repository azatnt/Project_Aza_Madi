from django.contrib import admin
from .models import *


class RestaurantAdmin(admin.ModelAdmin):
    class Meta:
        model = Restaurants

class FoodsAdmin(admin.ModelAdmin):
    class Meta:
        model = Foods

admin.site.register(Restaurants)
admin.site.register(Foods)

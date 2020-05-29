from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class Food_Category_Admin(admin.ModelAdmin):
    class Meta:
        model = Food_Category


admin.site.register(Food_Category, Food_Category_Admin)

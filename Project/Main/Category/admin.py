from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)

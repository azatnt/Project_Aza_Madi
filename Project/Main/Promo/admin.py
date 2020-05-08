from django.contrib import admin
from .models import *


class PromoAdmin(admin.ModelAdmin):
    class Meta:
        model = Promo


admin.site.register(Promo, PromoAdmin)

from django.shortcuts import render
from .models import *




def promo_list(request):
    promo = Promo.objects.all()
    return render(request, 'promo/promo_list.html', context={'promo':promo})

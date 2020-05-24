from django.shortcuts import render
from .models import *




def promo_list(request):
    promo = Promo.objects.all()
    template = 'promo/promo_list.html'
    context = {
        'promo':promo
    }
    return render(request, template, context)

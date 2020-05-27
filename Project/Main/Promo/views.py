# from django.shortcuts import render
# from .models import *
# from django.views.generic import View
# from django.shortcuts import get_object_or_404
#
#
# 
# class PromoList(View):
#     def get(self, *args, **kwargs):
#         promo = Promo.objects.all()
#         template = 'promo/promo_list.html'
#         context = {
#             'promo':promo
#         }
#         return render(request, template, context)
#
#
# def promo_list(request):
#     promo = Promo.objects.all()
#     template = 'promo/promo_list.html'
#     context = {
#         'promo':promo
#     }
#     return render(request, template, context)

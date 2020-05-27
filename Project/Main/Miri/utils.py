from django.shortcuts import get_object_or_404
from django.shortcuts import render
from Promo.models import *
from Category.models import *



class ObjectDetailMixin:
    model = None
    template = None


    def get(self, request, slug):
		obj = get_object_or_404(self.model, slug__iexact=slug)
		obj_name = get_object_or_404(self.model, slug=slug)
		obj_name = self.model.objects.filter(slug=slug)
		food = Foods.objects.all()
		template = 'Miri/restaurant_detail.html'
		context = {
			'food':food,
			'restaurant':restaurant,
			'rest_name':rest_name
		}
		return render(request, template, context)

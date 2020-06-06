from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .utils import *
from Cart.models import *
from User.forms import *
from User.models import UserAddress






def checkout(request):
    try:
        the_id = request.session['cart_id'] #if there will be cart with it's related id, we will get it
        cart = Cart.objects.get(id=the_id)
        print (cart)
    except:
        the_id = None
        return HttpResponseRedirect(reverse('cart_url'))


    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.final_total = cart.total
        new_order.save()
    except:
        return HttpResponseRedirect(reverse('cart_url'))


    address_form = UserAddressForm(request.POST)
    if address_form.is_valid():
        new_address = address_form.save(commit=False)
        new_address.user = request.user
        new_address.save()
        return render(request, 'order/final_checkout.html', context={})



    # new_order, created = Order.objects.get_or_create(cart=cart)
    # if created:
    #     now = timezone.now()
    #     new_order.order_id = id_generator() #str(now)
    #     new_order.save()
    # new_order.user = request.user
    # new_order.save()

    if new_order.status == 'Courier Taking':
        # cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse('cart_url'))

    return render(request, 'order/order.html', context={'address_form':address_form})

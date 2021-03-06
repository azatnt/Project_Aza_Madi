from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from .models import *
from Restaurants.models import *
from Miri.views import *
from django.views.generic import View, DeleteView
from django.shortcuts import get_object_or_404




def cart(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None

    if the_id:
        new_total = 0
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
        cart.total = new_total
        # cart.user = request.user
        # we will do that after ordering,
        #when we will set statul=Ready, I will include this line of code, to identify which user's cart was ready
        cart.save()
        request.session['items_total'] = cart.cartitem_set.count()
        context = {'cart':cart}
    else:
        empty_message = 'Your cart is empty, Please keep shopping'
        context = {'empty':True, 'empty_message':empty_message}

    return render(request, 'cart/cart.html', context)



class RemoveFromCart(View):
    def get(self, request, id):
        try:
            the_id = request.session['cart_id']
            cart = Cart.objects.get(id=the_id)
        except:
            return HttpResponseRedirect(reverse('cart_url'))
        cartitem = CartItem.objects.get(id=id)
        cartitem.delete()
        return HttpResponseRedirect(reverse('cart_url'))






def update_cart(request, slug):
    request.session.set_expiry(400)

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login_url'))
    else:
        try:
            qty = session.GET.get('qty')
            update_qty = True
        except:
            qty = None
            update_qty = False

        try:
            the_id = request.session['cart_id']
        except:
            new_cart = Cart()
            new_cart.save()
            request.session['cart_id'] = new_cart.id
            the_id = new_cart.id
        cart = Cart.objects.get(id=the_id)

        try:
            product = Foods.objects.get(slug=slug)
        except Food.DoesNotExist:
            pass
        except:
            pass

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        request.session['items_total'] = cart.cartitem_set.count()
        cart_item.quantity += 1
        cart_item.save()

        if update_qty and qty:
            if int(qty) == 0:
                cart_item.delete()
            else:
                cart_item.quantity = qty
                cart_item.save()
        else:
            pass

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(reverse('cart_url'))

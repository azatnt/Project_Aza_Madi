from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from .models import *
from Restaurants.models import *
from Miri.views import *





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
        cart.save()
        request.session['items_total'] = cart.cartitem_set.count()
        context = {'cart':cart}
    else:
        empty_message = 'Your cart is empty, Please keep shopping'
        context = {'empty':True, 'empty_message':empty_message}

    return render(request, 'cart/cart.html', context)



def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse('cart_url'))

    cartitem = CartItem.objects.get(id=id)
    cartitem.delete()
    return HttpResponseRedirect(reverse('cart_url'))



def update_cart(request, slug):
    request.session.set_expiry(900)
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



    try:
        rest = Restaurants.objects.get(slug=slug)
    except Restaurants.DoesNotExist:
        pass
    except:
        pass



    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        print('Created')
    request.session['items_total'] = cart.cartitem_set.count()
    print(cart_item)
    cart_item.quantity += 1
    cart_item.save()
    print(cart_item)

    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass



        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # return redirect('restaurant_detail_url', slug=)


    return HttpResponseRedirect(reverse('cart_url'))

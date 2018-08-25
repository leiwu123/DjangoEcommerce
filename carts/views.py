from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart


# def cart_create(user=None):
#     cart_obj = Cart.new_cart()
#     return cart_obj


def cart_home(request):
    # cart_obj, new_obj = Cart.objects.new_or_get(request)
    # products = cart_obj.products.all()
    # total = 0
    # for x in products:
    #   total += x.price
    # print(total)
    # cart_obj.total = total
    # cart_obj.save()
    # cart_id = request.session.get("cart_id", None)
    # print(cart_id)
    # qs = Cart.objects.filter(id=cart_id)
    # if qs.count() == 1:
    #     cart_obj = qs.first()
    #     if request.user.is_authenticated() and cart_obj.user is None:
    #       cart_obj.user = request.user
    #       cart_obj.save()
    # else:
    #     cart_obj = Cart.objects.new(user=request.user)
    #     request.session['cart_id'] = cart_obj.id
    return render(request, "carts/home.html", {})


def cart_update(request):
  product_id = 6
  product_obj = Product.objects.get(id=product_id)
  cart_obj, new_obj = Cart.objects.new_or_get(request)
  cart_obj.products.add(product_obj) # cart_obj.products.add(product_id)
  # cart_obj.title = "new title"
  # cart_obj.save()
  # cart_obj.products.remove(product_obj)
  # return redirect(product_obj.get_absolute_url())
  return redirect("cart:home")
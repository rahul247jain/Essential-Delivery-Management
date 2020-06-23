from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from cart.cart import Cart
from users.models import User
from .models import Warehouse, KeyVal


def searchproducts(request):
    cart = Cart(request)
    if request.user.is_authenticated:
        user_id = request.user.id
        current_user_object = User.objects.get(id=user_id)
        warehouses = Warehouse.objects.all()
        dis = []
        for item in cart:
            for wh in warehouses:
                wareitem = get_object_or_404(
                    KeyVal, locname_id=wh, product=item['product'])
                dis.append(wareitem)

        return render(request, 'delivery_area.html', {'waredis': dis})

    return render(request, 'delivery_area.html')

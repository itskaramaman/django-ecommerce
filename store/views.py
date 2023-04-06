from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *

def main(request):
    """
    Main View of store displaying all the items
    """
    context = {}
    return render(request, "store/main.html", context)

def store(request):
    '''
    This function shows all the products listed on the store.
    '''

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order_items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        order_items = []
        order = None
        cart_items = 0

    context = {"order_items": order_items, "order": order, "cart_items": cart_items}
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "store/store.html", context)

def checkout(request):
    shipping = False
    customer = None
    total = 0
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order_items = order.orderitem_set.all()
        shipping = order.shipping
        total = order.get_cart_total
    print(total)
    context = {'order_items': order_items, 'order': order, 'shipping': shipping, 'customer': customer, 'total': total}
    return render(request, "store/checkout.html", context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order_items = order.orderitem_set.all()
    else:
        order_items = []
        order = None
    context = {"order_items": order_items, "order": order}
    return render(request, "store/cart.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        order_item.quantity = order_item.quantity + 1
    elif action == "remove":
        order_item.quantity = order_item.quantity - 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False,
            )
        total = float(data['userFormData']['total'])

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shippingFormData']['address'],
                city=data['shippingFormData']['city'],
                state=data['shippingFormData']['state'],
                zipcode=data['shippingFormData']['zipcode'],
            )
    else:
        print("User not logged in")
    return JsonResponse('Payment Complete', safe=False)

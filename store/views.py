from django.shortcuts import render
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
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "store/store.html", context)

def checkout(request):
    context = {}
    return render(request, "store/checkout.html", context)

def cart(request):
    context = {}
    return render(request, "store/cart.html", context)
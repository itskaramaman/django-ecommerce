from django.urls import path
from .views import cart, checkout, main, store

urlpatterns = [
    path("", store, name="store"),
    path("checkout/", checkout, name="checkout"),
    path("cart/", cart, name="cart")
]

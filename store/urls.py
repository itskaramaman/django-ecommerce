from django.urls import path
from .views import cart, checkout, store, updateItem, processOrder

urlpatterns = [
    path("", store, name="store"),
    path("checkout/", checkout, name="checkout"),
    path("cart/", cart, name="cart"),
    path("update-item/", updateItem, name="update_item"),
    path("process-order/", processOrder, name="process_item")
]

from django.urls import path
from . import views
urlpatterns = [
    path('',views.cart ,name = 'cart'),
    path('add_cart/<product_id>/',views.add_cart ,name = 'add_cart'),
    path('remove_cart/<product_id>/',views.remove_cart ,name = 'remove_cart'),
    path('remove_cart_item/<product_id>/',views.remove_cart_item ,name = 'remove_cart_item'),
    path('place-order.html',views.placeorder ,name = 'placeorder'),
]


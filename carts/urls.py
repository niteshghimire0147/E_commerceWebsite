from os import name
from django.urls import path
from . import views
from .views import (
    ItemDetailView,
    CheckoutView,
    
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,

    AddCouponView,
    RequestRefundView,
    add_to_index,
    remove_from_index,
)

urlpatterns = [
    
    path('add_to_index/<slug>/', add_to_index, name='add_to_index'),
    path('remove_from_index/<slug>/', remove_from_index, name='remove_from_index'),


    

    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('cart/', OrderSummaryView.as_view(), name='cart'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('Review_rate/<int:id>/', views.Review_rate, name='Review_rate'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),

    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    
]
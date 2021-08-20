from os import name
from django.urls import path
from . import views
from .views import (
    
    ProductView,
)


urlpatterns = [
    path('', views.home, name='index'),
    path('contact', views.contact, name='contact'),
    path('product/', ProductView.as_view(), name='product'),
    path('pro/', views.products_list, name='products_list'),
]
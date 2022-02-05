from unicodedata import name
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('product_single/<int:pk>/', product_single, name="product_single"),
    path('product_single_discount/<int:pk>/', product_single_discount, name='product_single_discount'),
    path('add_product/', add_product, name='add_product'),
    path('adds_product/', adds_product, name='adds_product'),
    path('cart/', cart, name='cart'),
    path('qrcodes/', qrcodes, name='qrcodes'),
    path('category/<int:id>/', category, name='category'),
    path('add-discount-product/', add_discount__product, name='add_discount__product'),
    path('adds_discount__product/', adds_discount__product, name='adds_discount__product')
]

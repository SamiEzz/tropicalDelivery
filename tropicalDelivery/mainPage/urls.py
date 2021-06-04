from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('p/', views.getProducts, name='products'),
    path('products/', views.products, name='products'),
    path('home/', views.home, name='home'),
    #path('cart/', views.cart, name='cart'),


]

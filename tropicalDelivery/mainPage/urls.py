from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('p/', views.getProducts, name='products'),
    path('products/', views.products, name='products'),

]

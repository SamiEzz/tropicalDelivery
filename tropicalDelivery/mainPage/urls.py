from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('p/', views.getProducts, name='products'),
    path('products/', views.products, name='products'),
    #path('.well-known/pki-validation/87D1915D0CC29BE6B8B3CBFC8F516BC6.txt', views.ssl, name='ssl'),
]

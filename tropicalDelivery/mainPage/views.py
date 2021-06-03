from .models import Product
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("Hello, world. You're at the mainPage index.")


def getProducts(request):
    output = "title,description,image,price,providerId \n"
    all_product_list = Product.objects.all()
    for p in all_product_list:
        output += p.title + ","
        output += p.description + ","
        output += p.image + ","
        output += str(p.price) + ","
        output += str(p.providerId) + "\n"
    return HttpResponse(output)


def products(request):
    all_product_list = Product.objects.all()
    template = loader.get_template('mainPage/getProducts.html')
    context = {
        'all_product_list': all_product_list,
    }
    return HttpResponse(template.render(context, request))

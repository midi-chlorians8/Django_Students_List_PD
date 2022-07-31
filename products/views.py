from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})
    # return HttpResponse('Hello Word')

def nprod(request):
    return HttpResponse('New item')

def jl(request):
    products = Product.objects.all()
    res = '<h1>Cписок товаров<h1>'
    for item in products:
        res += f'<p>{item.id} {item.name}</p>\n'
    return HttpResponse(res)


from .models import Product

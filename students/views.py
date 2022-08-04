from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    products = Students.objects.all()
    res = '<h1>Cписок студов:<h1>'
    for item in products:
        res += f'<p>{item.id} {item.name} {item.type}</p>\n'
    return HttpResponse(res)


def studslist(request):
    students = Students.objects.all()
    return render(request, 'justlist.html',
                  {'students': students})


def jl(request):
    products = Students.objects.all()
    res = '<h1>Cписок товаров<h1>'
    for item in products:
        res += f'<p>{item.id} {item.name} {item.type}</p>\n'
    return HttpResponse(res)


from .models import Students

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return render(request, 'startindex.html')


def abc(request):
    return HttpResponse('New item')

def testhtml(request):
    return render(request, 'abc.html')


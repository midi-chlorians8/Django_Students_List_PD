from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('new', views.nprod),
    path('jl', views.jl)
]
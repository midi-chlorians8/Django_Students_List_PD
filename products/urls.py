from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="template_products")
    # path('new', views.nprod),
    # path('jl', views.jl)
]
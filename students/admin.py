from django.contrib import admin
from .models import Students
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

admin.site.register(Students, ProductAdmin)

from unicodedata import name
from django.contrib import admin
from .models import Product,Rack
from django.contrib.auth.models import Group

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity',)
    list_filter = ['category']

class RackAdmin(admin.ModelAdmin):
    list_display = ('rack', 'product', 'rack_quantity',)
    list_filter = ['product']

# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(Rack, RackAdmin)
#admin.site.register(Rack)
#admin.site.unregister(Product)
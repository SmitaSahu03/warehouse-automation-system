from django import forms
from .models import Product, Rack

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category' , 'quantity']

class RackForm(forms.ModelForm):
    class Meta:
        model = Rack
        fields = ['rack', 'product' , 'rack_quantity']
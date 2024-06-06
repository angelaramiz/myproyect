from django import forms 
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price','image_url','description','comments','related_products']
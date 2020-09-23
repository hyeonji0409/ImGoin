from django import forms
from .models import Product

class ProductPost(forms.ModelForm):
    class Meta:
        model =  Product
        fields = ['title', 'body']


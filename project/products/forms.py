from django import forms

from .models import product

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ('description', 'price', 'quantity')
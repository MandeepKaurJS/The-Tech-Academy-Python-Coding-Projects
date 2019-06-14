from django.forms import  ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model=Product
        #fecthing all values with dunder
        fields='__all__'


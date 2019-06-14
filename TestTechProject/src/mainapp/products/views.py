from django.shortcuts import render
from .models import Product
# Create your views here.
def admin_console(request):
    #a variable we store values
    products=Product.objects.all()
    return render(request,'products/products_page.html',{'products':products})
from django.shortcuts import render
from .models import Product
# from django.views.generic import ListView, DetailView

# Create your views here.
def Product_all(request):
    products = Product.objects.all()
    return render(request, 'products/product_all.html', {'products': products})

def Product_detail(request, product_id):
    product = Product.objects.get( id=product_id) 
    x={'product': product}
    return render(request, 'products/product_detail.html',x)



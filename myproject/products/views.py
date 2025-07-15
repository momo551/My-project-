from django.shortcuts import render
from .models import Product
# from django.views.generic import ListView, DetailView

# Create your views here.
def Product_list(request):
    Products = Product.objects.all()
    return render(request, 'products/product_all.html', {'products': Products})

def Product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})


# def Product_list_view(ListView):
#     model = Product
#     template_name = 'products/product_all.html'
#     context_object_name = 'products'

# def Product_detail_view(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.Product_list, name='product_all'),
    path('products/<int:product_id>/', views.Product_detail, name='product_detail'),
]


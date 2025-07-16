from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'updated_at', 'image', 'active', 'category','description')
    search_fields = ('name',)
    


admin.site.register(Product, ProductAdmin)
admin.site.site_header = 'Mohamed Abed Admin'
admin.site.site_title = 'Mohamed Abed control panel'

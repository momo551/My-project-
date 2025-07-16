from django.db import models

# Create your models here.
class Product(models.Model):
    x=[
        ('Supplements', 'Supplements'),
        ('Clothing', 'Clothing'),
        ('Books', 'Books'),
    ]


    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=50.00)
    description = models.TextField(null=True, blank=True,verbose_name="Product Description")
    image = models.ImageField(upload_to='products/%y/%m/%d',verbose_name='Product Image')
    active = models.BooleanField(default=True, verbose_name='Active')
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, default='General', verbose_name='Category',null=True, blank=True,choices=x)
    def __str__(self):
        return self.name
    

class Meta:
    ordering = ['name']
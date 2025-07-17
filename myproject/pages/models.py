from django.db import models

# Create your models here.

class Login(models.Model):
    username= models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    password= models.CharField(max_length=100)
    def __str__(self):
        return self.username
from django.shortcuts import render
from . form import  LoginModelForm , Login
from . models import Login
from products.models import Product
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = LoginModelForm(request.POST)
        if form.is_valid():
            # حفظ البيانات في قاعدة البيانات
            login_instance = form.save()

            # استخراج البيانات بعد الحفظ
            username = login_instance.username
            email = login_instance.email
            password = login_instance.password
            print(f"Username: {username}, Email: {email},Password: {password}")

            products = Product.objects.filter(active=True).order_by('-updated_at')
            return render(request,'pages/about.html',{'username': username, 'email': email, 'products': products})
    else:
        form = LoginModelForm()
    return render(request, 'pages/index.html', {'form': form})

def user_list(request):
    users = Login.objects.all()
    return render(request, 'pages/user_list.html', {'users': users})


def about(request):
    products = Product.objects.filter(active=True).order_by('-updated_at')
    username = request.user.username if request.user.is_authenticated else ' add'
    return render(request, 'pages/about.html',{'products': products, 'username': username})
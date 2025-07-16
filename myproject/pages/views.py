from django.shortcuts import render
from . form import LoginForm, LoginModelForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = LoginModelForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Here you can handle the login logic, e.g., authenticate the user
            print(f"Username: {username}, Password: {password}")
            return render(request,'pages/about.html',{'username': username})
    else:
        form = LoginModelForm()
    return render(request, 'pages/index.html', {'form': form})



def about(request):

    return render(request, 'pages/about.html')
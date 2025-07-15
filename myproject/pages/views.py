from django.shortcuts import render

# Create your views here.

def index(request):
    # if request.method == 'POST':
    #     # Handle POST request logic here
    #     return render(request, 'pages/index.html')
    
    return render(request,'pages/index.html')

def about(request):

    return render(request, 'pages/about.html')
from django.shortcuts import render

# Create your views here.

def index(request):
    x={
        'title': 'Welcome to My Page',
        'message': 'This is the index page of my Django application.'
    },
    return render(request,'pages/index.html')

def about(request):
    if request.method == 'POST':
        # Handle POST request logic here
        return render(request, 'pages/about.html')

    return render(request, 'pages/about.html')
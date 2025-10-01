from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages 

def home(request):
    products = Product.objects.all().order_by("date")
    return render(request, 'files/products.html', {'products':products})

def about(request):
    return render(request, 'files/about.html' )

@csrf_protect
def login_user(request):
    c = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # message.success(request, "you have been logged in")
            return redirect('home')
        else:
            # message.success(request, "username or password us incorrect ")
            return redirect('login')
    else:
            return render(request, 'files/login.html')

def logout_user(request):
    logout(request)
    # message.success(request, "you have been logged out")
    return redirect('home')
    
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages

def home(request):
    email = ""
    data = {
        'email': email
    }
    return render(request, 'main/home.html',data)


def register(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # validation for unique email

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'main/register.html')
        
        new_user = User(
            name=name,
            email=email,
            password=password
        )
        new_user.save()

        return redirect('/')

    else:
        return render(request, 'main/register.html')


def login(request):
    if request.method == 'POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email, password=password).exists():
            return redirect('/')
        else:
            messages.error(request, "Email or/and Password is incorrect")
            return render(request, 'main/login.html')

    else:
        return render(request, 'main/login.html')

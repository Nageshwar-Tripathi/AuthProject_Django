from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages

def home(request):
    return render(request, 'main/home.html')


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
    return render(request, 'main/login.html')

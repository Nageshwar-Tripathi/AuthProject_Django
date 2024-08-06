from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Post
from django.contrib import messages

def home(request):

    if request.session.has_key('logged'):
        email = request.session['logged']

        user = User.objects.get(email=email)

        all_posts = Post.objects.all()

        data = {
            'user': user ,
            'posts': all_posts,
        }
        return render(request, 'main/home.html',data)
    else:
        return redirect('/login/')


def register(request):
    if request.session.has_key('logged'):
        return redirect('/')
    else:
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
            request.session['logged'] = email
            return redirect('/')

        else:
            return render(request, 'main/register.html')


def login(request):
    if request.session.has_key('logged'):
        return redirect('/')
    else:
        if request.method == 'POST':
            
            email = request.POST.get('email')
            password = request.POST.get('password')

            if User.objects.filter(email=email, password=password).exists():
                request.session['logged'] = email
                return redirect('/')
            else:
                messages.error(request, "Email or/and Password is incorrect")
                return render(request, 'main/login.html')

        else:
            return render(request, 'main/login.html')



def logout (request):
    if request.session.has_key('logged'):
        del request.session['logged']
    
    return redirect('/login/')
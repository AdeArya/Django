from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'title': 'home',
    }

    return render(request, 'index.html', context)

def loginView(request):
    context = {
        'title': 'login',
    }

    if request.method == 'POST':
        usernames = request.POST['username']
        passwords = request.POST['password']

        user = authenticate(username=usernames, password=passwords) 
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, 'login.html', context)

def logoutView(request):
    context = {
        'title': 'logout',
    }

    if request.method == 'POST':
        if request.POST['logout'] == 'Submit Query':
            logout(request)
            return redirect('index')
    
    return render(request, 'logout.html', context)

def registerView(request):
    
    context = {
        'title': 'register',
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'register.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'title': 'home'.upper(),
    }


    return render(request, 'index.html', context)

def login(request):
    context = {
        'title': 'login'.upper(),
    }

    if request.method == 'POST':
        usernames = request.POST['username']
        passwords = request.POST['password']

        user = authenticate(username=usernames, password=passwords)

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    # if request.method == 'GET':
    #     if request.user.is_authenticated:
    #         return redirect('index')
    #     else:
    return render(request, 'login.html', context)
@login_required
def logout(request):
    context = {
        'title': 'logout',
    }

    if request.method == 'POST':
        if request.POST['logout'] == 'Submit Query':
            auth_logout(request)
            return redirect('index')

    return render(request, 'logout.html', context)

def register(request):
    
    context = {
        'title': 'register'.upper(),
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)

        return redirect('index')
    

    return render(request, 'register.html', context)
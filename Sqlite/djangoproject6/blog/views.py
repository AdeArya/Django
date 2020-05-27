from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'page_title': 'blog',
    }

    template_name = None

    if request.user.is_authenticated:
        template_name = 'blog/index-user.html'
    else:
        template_name = 'blog/index-anon.html'
    
    return render(request, template_name, context)

def loginViews(request):
    context = {
            'page_title': 'login'.upper(),
        }
    
    if request.method == 'POST':
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(username=username_login, password=password_login)
        
        if user is not None:
            login(request, user)
            return redirect('blog:home-blog')
        else:
            return redirect('login')

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('blog:home-blog')
        else:
            return render(request, 'login.html', context)

@login_required
def logoutViews(request):
    context = {
        'page_title': 'logout'.upper()
    }

    if request.method == 'POST':
        if request.POST['logout'] == 'Submit Query':
            logout(request)
            return redirect('blog:home-blog')
    
    return render(request, 'logout.html', context)

def regViews(request):
    if request.method == 'POST':
        usernames = request.POST['usernames']
        passwords = request.POST['passwords']
        new_users = User.objects.create_user(username=usernames, password=passwords)
    

    context = {
        'page_title': 'register',

    }
    return render(request, 'reg.html', context)
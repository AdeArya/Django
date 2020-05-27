from django.shortcuts import render
from django.contrib.auth.views import LoginView

class Index(LoginView):
    template_name = 'index.html'
    

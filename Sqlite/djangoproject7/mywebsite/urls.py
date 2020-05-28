from django.contrib import admin
from django.urls import path
from . import views,liat

urlpatterns = [
    path('logout/', liat.logoutView, name='logout'),
    path('login/', liat.loginView, name='login'),
    path('register/', liat.registerView, name='register'),
    path('', liat.index, name='index'),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from .views import Index

urlpatterns = [
    path('blog/',include(('blog.urls','blog'), namespace='blog')),
    path('',Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
]

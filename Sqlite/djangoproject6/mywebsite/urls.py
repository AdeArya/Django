from django.contrib import admin
from django.urls import path, include
from blog.views import loginViews, logoutViews, regViews

urlpatterns = [
    path('reg/', regViews, name='register'),
    path('logout/', logoutViews, name='logout'),
    path('login/', loginViews, name='login'),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('admin/', admin.site.urls),
]

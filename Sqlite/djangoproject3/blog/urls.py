from django.urls import path
from django.conf.urls import url
from .views import IndexBlog, DetailBlog
from .models import ModelsListView

urlpatterns = [
    url(r'^detail/(?P<slug>[\w-]+)$', DetailBlog.as_view(), name = 'detail'),
    path('', IndexBlog.as_view(), name = 'index'),
]
from django.urls import path
from .views import ArtikelFormView,ArtikelListView

urlpatterns = [
    path('create/',ArtikelFormView.as_view(), name='create'),
    path('list/', ArtikelListView.as_view(), name='list')
]
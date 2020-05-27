from django.urls import path
from .views import ArticleListView, ArticleCreateView

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('', ArticleListView.as_view(), name='list'),
]
from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import Article
from .forms import ArticleForm

class ArticleListView(ListView):
    model = Article
    extra_context = {
        'page_title': 'List View Home' 
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)

class ArticleCreateView(CreateView):
    form_class = ArticleForm
    model = Article
    extra_context = {
        'page_title': 'Create View'
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)
    
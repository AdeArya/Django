from django.views.generic import ListView, DetailView

from .models import ModelsListView

class IndexBlog(ListView):
    model = ModelsListView
    extra_context = {
        'page_title': 'index blog'.upper()
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)

class DetailBlog(DetailView):
    model = ModelsListView
    extra_context = {
        'page_title': 'detail blog'.upper()
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)
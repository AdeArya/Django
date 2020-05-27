from django.views.generic import ListView
from .models import Artikel

class IndexListView(ListView):
    model = Artikel
    paginate_by = 2
    extra_context = {
        'page_title': 'List View',
    }

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)




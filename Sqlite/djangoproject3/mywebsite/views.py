from django.views.generic.base import TemplateView

class IndexHome(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'page_title': 'home class based view'.upper()
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return kwargs
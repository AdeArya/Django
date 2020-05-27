from django.views.generic.base import TemplateView

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = {
            'page_title': 'home index',
            'content': 'belajar menggunakan template view'
        }

        return context
from django.views.generic.base import TemplateView

# index home
class Index(TemplateView):

    template_name = 'index.html'
    
    # context return
    def get_context_data(self):
        context = {
            'title': 'home index',
            'body': 'home index dengan class based view'
        }

        return context
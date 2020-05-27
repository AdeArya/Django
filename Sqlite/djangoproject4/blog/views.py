from django.views.generic import FormView, ListView
from django.shortcuts import redirect
from django.urls import reverse
from .forms import ArtikelForm
from .models import Artikel

class ArtikelFormView(FormView):
    form_class = ArtikelForm
    template_name = 'blog/create.html'
    
    def get_success_url(self):
        return reverse('blog:list')
    
    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())

class ArtikelListView(ListView):
    model = Artikel

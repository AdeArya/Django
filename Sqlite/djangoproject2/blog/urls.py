from django.conf.urls import url
from .views import IndexListView

urlpatterns = [

    # regex harus berparameter page
    url(r'^(?P<page>\d+)$',IndexListView.as_view(), name='index'),
]
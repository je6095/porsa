from django.conf.urls import url, include
from . import views

app_name = 'directory'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customer_results$', views.customer_search, name='customer_search'),
]

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, index, getdata
from django.urls import path

app_name = CatalogConfig.name

urlpatterns = [
    path('index/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('home/', home, name='home'),
    path('contacts/getdata/', getdata, name='getdata'),
    ]

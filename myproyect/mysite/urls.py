from django.urls import path
from .views import add_product, index

urlpatterns = [
    path('',index, name='index'),
    path('add/', add_product, name='add_product'),

]

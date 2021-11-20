from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.CustomerList, name='CustomerList'),
    path('create_customer/', views.createCustomer, name='create_customer'),
    
]
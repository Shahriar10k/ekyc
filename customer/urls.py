from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.CustomerList, name='CustomerList'),
    path('create_customer/', views.createCustomer, name='create_customer'),
    path('delete_customer/', views.deleteCustomer, name='delete_customer'),
    path('update_customer/', views.updateCustomer, name='update_customer'),
    
]
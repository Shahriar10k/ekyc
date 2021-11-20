from django.urls import path
from . import views

urlpatterns = [

    path('create_customer/', views.createCustomer, name='create_customer'),
    
]
from django.urls import path


from . import views

urlpatterns = [

    path('create_entry/',views.createEntry, name='create_entry'),
    path('',views.StudentList,name='StudentList'),
    #path('addentry',views.addentry, name='addentry'),
    #path('editentry',views.editentry, name='editentry'),
    #path('deleteentry',views.deleteentry, name='deleteentry),
]
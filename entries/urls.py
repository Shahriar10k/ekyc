from django.urls import path


from . import views

urlpatterns = [

    path('create_entry/',views.createEntry, name='create_entry'),
    path('create_course/',views.createCourse, name='create_course'),
    path('update_entry<str:pk>/',views.updateEntry, name='update_entry'),
    path('',views.StudentList,name='StudentList'),
    path('student_entry/',views.studentEntry, name='student_entry'),
    #path('addentry',views.addentry, name='addentry'),
    #path('editentry',views.editentry, name='editentry'),
    #path('deleteentry',views.deleteentry, name='deleteentry),
]
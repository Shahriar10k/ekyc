from django.urls import path
from . import views

urlpatterns = [

    path('create_entry/', views.createEntry, name='create_entry'),
    path('create_course/', views.createCourse, name='create_course'),
    path('update_entry/', views.updateEntry, name='update_entry'),
    path('delete_entry/', views.deleteEntry, name='delete_entry'),
    path('student_entry/update_personal_info/', views.updatePersonalInfo, name='update_personal_info'),
    path('', views.StudentList, name='StudentList'),
    path('student_entry/', views.studentEntry, name='student_entry'),
    path('assign_grade/', views.assignGrade, name='assign_grade'),
    #path('addentry', views.addentry, name='addentry'),
    #path('editentry', views.editentry, name='editentry'),
    #path('deleteentry', views.deleteentry, name='deleteentry),
]
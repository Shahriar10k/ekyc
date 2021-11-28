from django.urls import path


from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('course_list',views.CourseList,name='course_list'),
    path('update_course',views.updateCourse,name='update_course'),
    path('delete_course',views.deleteCourse,name='delete_course'),
]
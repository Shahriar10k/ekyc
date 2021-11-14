from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from entries.models import Student_info
from entries.filters import StudentFilter


# Create your views here.

def createEntry(request) : 

    form1 = Student_info_form()
    
    if request.method == 'POST':
        form1 = Student_info_form(request.POST, request.FILES)     
        if form1.is_valid(): 
            form1.save()
            
            messages.success(request, "Saved")
            return redirect('dashboard')
            

    context = {'form1':form1 ,}

    return render(request, 'entries/add_entries.html', context)

#filter for student list
def StudentList(request):
    student_list = Student_info.objects.all()
    stuFilter = StudentFilter(request.GET, queryset = student_list)
    student_list = stuFilter.qs

    context = {'student_list': student_list, 'stuFilter': stuFilter}
    return render(request, 'entries/student_list.html', context)

#@login_required
#def StudentProfile(request):
 #   pass
  #  return render(request, 'student_list/Student_Profile.html')   
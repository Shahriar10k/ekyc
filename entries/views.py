from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from entries.models import *
from entries.filters import StudentFilter


# Create your views here.

def createEntry(request):
    form1 = Student_info_form()

    if request.method == 'POST':
        form1 = Student_info_form(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            f_nsu_id= form1.cleaned_data['nsu_id']
            stu_obj = Student_info.objects.get(nsu_id=f_nsu_id)
            stu_uid = stu_obj.id
            stu_u_obj = Student_info.objects.get(id=stu_uid)
            print(stu_uid)
            context = {'stu_uid': stu_u_obj}
            messages.success(request, "Student Entry Created")
            return render(request, 'entries/student_entry.html', context)

    context = {'form1': form1, }

    return render(request, 'entries/add_entries.html', context)


# filter for student list
def StudentList(request):
    student_list = Student_info.objects.all()
    stuFilter = StudentFilter(request.GET, queryset=student_list)
    student_list = stuFilter.qs

    context = {'student_list': student_list, 'stuFilter': stuFilter}
    return render(request, 'entries/student_list.html', context)


# Student profile General Info
def studentEntry(request):
    viewdetailsID = request.POST.get('viewdetailsID')
    stu_obj = Student_info.objects.get(nsu_id=viewdetailsID)
    stu_uid = stu_obj.id
    stu_u_obj = Student_info.objects.get(id=stu_uid)            #fetching uid object of student info
    stu_obj_ssc = Ssc_equivlent.objects.get(id=stu_uid)       #fetching uid object of ssc
    stu_obj_hsc = Hsc_equivlent.objects.get(id=stu_uid)       #fetching uid object of hsc
    stu_obj_financial = Financial_history.objects.get(id=stu_uid)       # fetching uid object of financial 'stu_financial': stu_u_obj_financial
    context = {'stu_uid': stu_u_obj, 'stu_ssc': stu_obj_ssc, 'stu_hsc': stu_obj_hsc, 'stu_financial': stu_obj_financial}
    return render(request, 'entries/student_entry.html', context)


# @login_required
# def StudentProfile(request):
#   pass
#  return render(request, 'student_list/Student_Profile.html')

def updateEntry(request, pk):
    student = Student_info.objects.get(id=pk)
    form1 = Student_info_form(instance=student)

    if request.method == 'POST':
        form1 = Student_info_form(request.POST, request.FILES, instance=student)
        if form1.is_valid():
            form1.save()

            messages.success(request, "Saved")
            return redirect('dashboard')

    context = {'form1': form1, }
    return render(request, 'entries/update_entries.html', context)


def createCourse(request):
    form1 = Course_form()

    if request.method == 'POST':
        form1 = Course_form(request.POST)
        if form1.is_valid():
            form1.save()

            messages.success(request, "Saved")
            return redirect('dashboard')

    context = {'form1': form1, }

    return render(request, 'entries/add_course.html', context)

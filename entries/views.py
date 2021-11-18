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
            f_stu_id = form1.cleaned_data['nsu_id']
            
            global cEntGetStuID
            def cEntGetStuID():
                return f_stu_id

            return redirect('student_entry')

    context = {'form1': form1, }

    return render(request, 'entries/add_entries.html', context)

#update entry
def updateEntry(request): 

    #if POST coming from student list "edit" button then fetch intance using uuid
    if 'viewdetailsID' in request.POST:
        uid = request.POST.get('viewdetailsID')
        student = Student_info.objects.get(id=uid)
        form1 = Student_info_form(instance=student)
    #if POST coming from editing the form then fetch instance using nsu id 
    else:
        nsu_id= request.POST.get('nsu_id')
        student=Student_info.objects.get(nsu_id=nsu_id)
        form1 = Student_info_form(instance=student)
    context = {'form1': form1, }
    

    if request.method == 'POST' :
        form1 = Student_info_form(request.POST, request.FILES, instance=student)
        print("here")
        print(form1)
        if form1.is_valid():
            form1.save()

            #use the input nsu id to fetch student
            f_nsu_id= form1.cleaned_data['nsu_id']
            stu_obj = Student_info.objects.get(nsu_id=f_nsu_id)
            stu_uid = stu_obj.id
            stu_u_obj = Student_info.objects.get(id=stu_uid)
            context = {'stu_uid': stu_u_obj}
            messages.success(request, "Student Entry Updated")
            return render(request, 'entries/student_entry.html', context)

    
    
    return render(request, 'entries/update_entries.html', context)


# filter for student list
def StudentList(request):
    student_list = Student_info.objects.all()
    stuFilter = StudentFilter(request.GET, queryset=student_list)
    student_list = stuFilter.qs

    context = {'student_list': student_list, 'stuFilter': stuFilter}
    return render(request, 'entries/student_list.html', context)

# Student profile General Info
def studentEntry(request):
    
    if request.method == 'POST':
        stu_id = request.POST.get('viewdetailsID')
    else:
        stu_id = cEntGetStuID()
    
    stu_obj = Student_info.objects.get(nsu_id=stu_id)
    stu_uid = stu_obj.id
    # fetching uid object of student info
    stu_u_obj = Student_info.objects.get(id=stu_uid)
    context = {'stu_uid': stu_u_obj}

    # checking if there is an entry for the selected id in DB > Personal_info
    if Personal_info.objects.filter(id=stu_uid).exists():
        stu_per_info_obj = Personal_info.objects.get(id=stu_uid)  # fetching student's personal information
        context['stu_personal'] = stu_per_info_obj
    
    # checking if there is an entry for the selected id in DB > Ssc_equivlent
    if Ssc_equivlent.objects.filter(id=stu_uid).exists():
        stu_ssc_info_obj = Ssc_equivlent.objects.get(id=stu_uid)  # fetching ssc/equivalent academic information
        context['stu_ssc'] = stu_ssc_info_obj

    # checking if there is an entry for the selected id in DB > Hsc_equivlent
    if Hsc_equivlent.objects.filter(id=stu_uid).exists():
        stu_hsc_info_obj = Hsc_equivlent.objects.get(id=stu_uid)  # fetching hsc/equivalent academic information
        context['stu_hsc'] = stu_ssc_info_obj

    # checking if there is an entry for the selected id in DB > Financial_info
    if Financial_info.objects.filter(id=stu_uid).exists():
        stu_fin_info_obj = Financial_info.objects.get(id=stu_uid)  # fetching financial information
        context['stu_financial'] = stu_fin_info_obj

    # checking if there is any entry against the selected id in DB > Grade
    if Grade.objects.filter(id=stu_uid).exists():
        stu_grade_info_obj = Grade.objects.get(id=stu_uid)  # fetching financial information
        context['stu_grade'] = stu_grade_info_obj

    return render(request, 'entries/student_entry.html', context)



# @login_required
# def StudentProfile(request):
#   pass
#  return render(request, 'student_list/Student_Profile.html')


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

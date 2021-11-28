from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from entries.models import *
from entries.filters import StudentFilter


# Create your views here.

mydata = {} # dictionary to store session data

def createEntry(request):
    form1 = Student_info_form()

    if request.method == 'POST':
        form1 = Student_info_form(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            f_nsu_id = form1.cleaned_data['nsu_id']
            
            # fetch UUID of the student from database using nsu-id from form
            stu_obj = Student_info.objects.get(nsu_id=f_nsu_id)
            stu_uid = stu_obj.id
            
            # store student's uuid for later use in the session
            mydata['stu_uid'] = stu_uid

            messages.success(request, f'Student Entry Created.')
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
        mydata['stu_uid'] = uid
    #if POST coming from editing the form then fetch instance using globally stored uuid
    else:
        uid = mydata['stu_uid']
        student = Student_info.objects.get(id=uid)
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
            return redirect('student_entry')

    return render(request, 'entries/update_entries.html', context)

# delete an entry
def deleteEntry(request):
    if 'id' in request.POST:
        stu_id = request.POST.get('id')
        #print(stu_id)

    student = Student_info.objects.get(nsu_id=stu_id)
    student.delete()

    messages.success(request, f'Entry Successfully Deleted.')
    return redirect('StudentList')

# view for updating personal information
def updatePersonalInfo(request):
    if 'viewdetailsID' in request.POST:
        stu_uid = request.POST.get('viewdetailsID')
    
        # store student's uuid for later use in the session
        mydata['stu_uid'] = stu_uid

        # create an entry against the 'stu_uid' in Personal_info model if it doesn't exist
        if not Personal_info.objects.filter(id_id=stu_uid).exists():
            student = Personal_info(id_id=stu_uid)
            student.save()
            print('does not exist')

    # access student's uuid which was stored above
    stu_uid = mydata['stu_uid']

    student = Personal_info.objects.get(id_id=stu_uid)
    form = Personal_info_form(instance=student)
    
    context = {'form' : form}

    if request.method == 'POST':
        form = Personal_info_form(request.POST, instance=student)
        if form.is_valid():
            form.save()

            messages.success(request, f'Personal Information Updated.')
            return redirect('student_entry')
    else:
        form = Personal_info_form()
    return render(request, 'entries/update_personal_info.html', context)

# update ssc/equivalent academic info
def updateSSCEquivInfo(request):
    if 'viewdetailsID' in request.POST:
        stu_uid = request.POST.get('viewdetailsID')

        print(stu_uid)
    
        # store student's uuid for later use in the session
        mydata['stu_uid'] = stu_uid

        # create an entry against the 'stu_uid' in Ssc_equivlent model if it doesn't exist
        if not Ssc_equivlent.objects.filter(id_id=stu_uid).exists():
            student = Ssc_equivlent(id_id=stu_uid)
            student.save()
            print('does not exist')

    # access student's uuid which was stored above
    stu_uid = mydata['stu_uid']

    student = Ssc_equivlent.objects.get(id_id=stu_uid)
    form = Ssc_equivlent_form(instance=student)
    
    context = {'form' : form}

    if request.method == 'POST':
        form = Ssc_equivlent_form(request.POST, instance=student)
        if form.is_valid():
            form.save()

            print(f'form saved')
            print(stu_uid)

            messages.success(request, f'SSC/Equivalent Academic Information Updated.')
            return redirect('student_entry')
    else:
        form = Ssc_equivlent_form()
    return render(request, 'entries/update_aca_ssc_equiv_info.html', context)

# update hsc/equivalent academic info
def updateHSCEquivInfo(request):
    if 'viewdetailsID' in request.POST:
        stu_uid = request.POST.get('viewdetailsID')

        print(stu_uid)
    
        # store student's uuid for later use in the session
        mydata['stu_uid'] = stu_uid

        # create an entry against the 'stu_uid' in Hsc_equivlent model if it doesn't exist
        if not Hsc_equivlent.objects.filter(id_id=stu_uid).exists():
            student = Hsc_equivlent(id_id=stu_uid)
            student.save()
            print('does not exist')

    # access student's uuid which was stored above
    stu_uid = mydata['stu_uid']

    student = Hsc_equivlent.objects.get(id_id=stu_uid)
    form = Hsc_equivlent_form(instance=student)
    
    context = {'form' : form}

    if request.method == 'POST':
        form = Hsc_equivlent_form(request.POST, instance=student)
        if form.is_valid():
            form.save()

            print(f'form saved')
            print(stu_uid)

            messages.success(request, f'HSC/Equivalent Academic Information Updated.')
            return redirect('student_entry')
    else:
        form = Hsc_equivlent_form()
    return render(request, 'entries/update_aca_hsc_equiv_info.html', context)

# filter for student list
def StudentList(request):
    student_list = Student_info.objects.all().order_by('nsu_id')
    stuFilter = StudentFilter(request.GET, queryset=student_list)
    student_list = stuFilter.qs

    context = {'student_list': student_list, 'stuFilter': stuFilter}
    return render(request, 'entries/student_list.html', context)

# Student profile General Info
def studentEntry(request):
    
    # if accessed from Student List page
    if request.method == 'POST':
        stu_id = request.POST.get('viewdetailsID')
        
        # fetch UUID from database using nsu-id from form
        stu_obj = Student_info.objects.get(nsu_id=stu_id)
        stu_uid = stu_obj.id

    # if accessed from an update function
    else:
        stu_uid = mydata['stu_uid']

    # fetching Student_info object of the student using UUID
    stu_u_obj = Student_info.objects.get( id=stu_uid )
    context = { 'stu_uid': stu_u_obj }

    # CGPA Calculation & passing to template
    cgpaCalculation(stu_uid)
    context['stu_cgpa'] = mydata['cgpa']
    context['stu_credit'] = mydata['credit']

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
        context['stu_hsc'] = stu_hsc_info_obj

    # checking if there is an entry for the selected id in DB > Financial_info
    if Financial_info.objects.filter(id=stu_uid).exists():
        stu_fin_info_obj = Financial_info.objects.get(id=stu_uid)  # fetching financial information
        context['stu_fin'] = stu_fin_info_obj

    # checking if there is any entry against the selected id in DB > Grade
    if Grade.objects.filter(id=stu_uid).exists():
        stu_grade_info_obj = Grade.objects.filter(id=stu_uid).order_by('year')
        #print(stu_grade_info_obj)
        context['stu_grade'] = stu_grade_info_obj       #pass grade obj

    return render(request, 'entries/student_entry.html', context)



# @login_required
# def StudentProfile(request):
#   pass
#  return render(request, 'student_list/Student_Profile.html')

def assignGrade(request):
    form1 = Grade_form()

    if request.method == 'POST':
        form1 = Grade_form(request.POST)
        if form1.is_valid():
            form1.save()

            messages.success(request, "Grade Information Added.")
            return redirect('dashboard')
    context = {'form1': form1,}
    return render(request, 'entries/assign_grade.html', context)


def updateFinancialInfo(request):
    if 'viewdetailsID' in request.POST:
        stu_uid = request.POST.get('viewdetailsID')
    
        # store student's uuid for later use in the session
        mydata['stu_uid'] = stu_uid

        # create an entry against the 'stu_uid' in Hsc_equivlent model if it doesn't exist
        if not Financial_info.objects.filter(id_id=stu_uid).exists():
            student = Financial_info(id_id=stu_uid)
            student.save()
            print('does not exist')

    # access student's uuid which was stored above
    stu_uid = mydata['stu_uid']

    student = Financial_info.objects.get(id_id=stu_uid)
    form = Financial_info_form(instance=student)
    
    context = {'form' : form}

    if request.method == 'POST':
        form = Financial_info_form(request.POST, instance=student)
        if form.is_valid():
            form.save()

            print(f'form saved')
            print(stu_uid)

            messages.success(request, f'Financial Info Updated.')
            return redirect('student_entry')
    else:
        form = Hsc_equivlent_form()
    return render(request, 'entries/update_financial_info.html', context)

# Calculate total credit passed & cgpa
def cgpaCalculation(uid):
    grade_points = Grade.objects.filter(id=uid)

    point_table = {
        'A': 4.00,
        'A-': 3.70,
        'B+': 3.30,
        'B': 3.00,
        'B-': 2.70,
        'C+':2.30,
        'C': 2.00,
        'C-': 1.70,
        'D+': 1.30,
        'D': 1.00,
        'F': 0.00,
    }

    credit_total= 0
    gpa_total = 0
    value = 0
    cgpa = 0

    for point in grade_points:                  #Grade*credit 4*3=12  12+11.1+12=35.1/9=3.9
        grade=point.grade

        if grade == 'W':
            pass
        elif grade == 'I':
            pass
        else:
            grade_point = point_table[grade]
            credit_count = point.course_code.course_credit

            credit_total += credit_count
            gpa_total += grade_point*credit_count

    if credit_total !=0:
        cgpa = gpa_total/credit_total

    value = "{:.2f}".format(cgpa)

    mydata['cgpa']=value
    mydata['credit'] = credit_total

#Edit Grade Information
def editGrade(request):
    #if POST coming from grade list "edit" button then fetch intance using gaid
    if 'grade_assign_id' in request.POST:
        gaid = request.POST.get('grade_assign_id')
        grade = Grade.objects.get(ga_id = gaid)
        uid = grade.id_id
        mydata['stu_uid'] = uid
        form = Grade_form(instance=grade)
        mydata['ga_id'] = gaid

    
    #if POST coming from editing the form then fetch instance using gaid 
    else:
        gaid = mydata['ga_id']
        grade = Grade.objects.get(ga_id = gaid)
        uid = grade.id_id
        mydata['stu_uid'] = uid
        form = Grade_form(instance= grade)
    context = {'form' : form}

    if request.method == 'POST':
        form = Grade_form(request.POST, instance = grade)
        if form.is_valid():
            form.save()
            messages.success(request, f"Grade Information Updated")
            return redirect("student_entry")

    return render(request, 'entries/edit_grade.html', context)

# delete a grade entry
def deleteGrade(request):
    if 'id' in request.POST:
        ga_id = request.POST.get('id')
        #print(ga_id)

    grade = Grade.objects.get(ga_id=ga_id)
    stu_uid = grade.id.id

    grade.delete()

    print(stu_uid)

    mydata['stu_uid'] = stu_uid

    messages.success(request, f'Grade Entry Successfully Deleted.')
    return redirect('student_entry')
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.

def createEntry(request) : 

    form1 = Student_info_form()
    form2 = Personal_info_form()
    form3 = Ssc_equivlent_form()
    form4 = Hsc_equivlent_form()
    form5 = Semester_history_form()
    form6 = Financial_history_form()

    if request.method == 'POST':
        form1 = Student_info_form(request.POST)
        form2 = Student_info_form(request.POST)
        form3 = Student_info_form(request.POST)
        form4 = Student_info_form(request.POST)
        form5 = Student_info_form(request.POST)
        form6 = Student_info_form(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid(): 
            form1.save()
            form2.save()
            form3.save()
            form4.save()
            form5.save()
            form6.save()

            messages.success(request, "Saved")
            return redirect('dashboard')
            

    context = {'form1':form1 , 'form2':form2 , 'form3':form3 , 'form4':form4 , 
            'form5':form5, 'form6':form6
                }

    return render(request, 'entries/add_entries.html', context)
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.

def createEntry(request) : 

    form1 = Student_info_form()
    
    if request.method == 'POST':
        form1 = Student_info_form(request.POST)
        
    
        if form1.is_valid() : 
            form1.save()
            
            messages.success(request, "Saved")
            return redirect('dashboard')
            

    context = {'form1':form1 , }

    return render(request, 'entries/add_entries.html', context)
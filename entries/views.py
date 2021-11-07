from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from .models import *
from .forms import *


# Create your views here.

def createEntry(request) : 
    
    context = {}

    return render(request, 'entries/add_entries.html', context)
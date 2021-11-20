from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.contrib import messages

from customer.filters import CustomerFilter
from .models import *
from customer.forms import *
from django.contrib.auth.decorators import login_required
from customer.models import *

# Create your views here.

#method for customer create
def createCustomer(request):
    form = Customer_info_form()

    if request.method == 'POST':
        form = Customer_info_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #f_nsu_id = form1.cleaned_data['nsu_id']
            
            # fetch UUID of the student from database using nsu-id from form
            #stu_obj = Student_info.objects.get(nsu_id=f_nsu_id)
            #stu_uid = stu_obj.id
            
            # store student's uuid for later use in the session
            #mydata['stu_uid'] = stu_uid

            messages.success(request, f'A New Customer Added.')
            return redirect('CustomerList')

    context = {'form': form, }

    return render(request, 'customer/create_customer.html', context)

# filter for customer list
def CustomerList(request):
    customer_list = Customer_info.objects.all().order_by('name')
    custFilter = CustomerFilter(request.GET, queryset=customer_list)
    customer_list = custFilter.qs

    context = {'customer_list': customer_list, 'custFilter': custFilter}
    return render(request, 'customer/customer_list.html', context)


# delete an entry
def deleteCustomer(request):
    if 'id' in request.POST:
        cust_id = request.POST.get('id')
        #print(stu_id)

    customer = Customer_info.objects.get(id=cust_id)
    customer.delete()

    messages.success(request, f'Customer Entry Successfully Deleted.')
    return redirect('CustomerList')
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.contrib import messages
import customer

from customer.filters import CustomerFilter
from .models import *
from customer.forms import *
from django.contrib.auth.decorators import login_required
from customer.models import *

# Create your views here.

my_data = {}

#method for customer create
def createCustomer(request):
    form = Customer_info_form()

    if request.method == 'POST':
        form = Customer_info_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()

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

#update customer information
def updateCustomer(request): 

    #if POST coming from customer list "edit" button then fetch intance using uuid
    if 'viewdetailsID' in request.POST:
        uid = request.POST.get('viewdetailsID')
        customer = Customer_info.objects.get(id=uid)
        form = Customer_info_form(instance=customer)
        my_data['cust_id'] = uid    #store uid for session
        print(uid)
    #if POST coming from editing the form then fetch instance using globally stored uid 
    else:
        uid = my_data['cust_id']
        customer=Customer_info.objects.get(id=uid)
        form = Customer_info_form(instance=customer)
    context = {'form': form, }
    

    if request.method == 'POST' :
        form = Customer_info_form(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

            messages.success(request, "Customer Information Updated")
            return redirect('CustomerList')

    return render(request, 'customer/update_customer.html', context)

def manageAccessPermission(request):
    if 'viewdetailsID' in request.POST:
        cust_id = request.POST.get('viewdetailsID')
        print(cust_id)
    
        my_data['cust_id'] = cust_id                # store customer's id for later use in the session

        # create an entry against the 'cust_id' in Customer_access_permission model if it doesn't exist
        if not Customer_access_permission.objects.filter(customer_id_id=cust_id).exists():
            customer = Customer_access_permission(customer_id_id=cust_id)
            customer.save()
            print('a new Customer_access_permission instance created')

    else:
        cust_id = my_data['cust_id']             # access customer's uuid which was stored above

    customer = Customer_access_permission.objects.get(customer_id=cust_id)
    form = Customer_access_permission_form(instance=customer)
    
    context = {'form': form}

    if request.method == 'POST':
        form = Customer_access_permission_form(request.POST, instance=customer)
        if form.is_valid():
            form.save()

            messages.success(request, f'Customer Access Permission Updated.')
            return redirect('CustomerList')
    else:
        form = Customer_access_permission_form()
    return render(request, 'customer/manage_access_permission.html', context)
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import *
from django import forms


class Customer_info_form(ModelForm):
    class Meta:
        model = Customer_info
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(Customer_info_form, self).__init__(*args, **kwargs)
        
        self.fields['file'].widget.attrs.update({'class': 'btn btn-outline-secondary '})
        self.fields['file'].required = True

class Customer_access_permission_form(ModelForm):
    class Meta:
        model = Customer_access_permission
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['customer_id'].label = "Customer's Name"
        self.fields['nsu_id'].label = 'NSU ID'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['father_name'].label = "Father's Name"
        self.fields['mother_name'].label = "Mother's Name"
        self.fields['date_of_birth'].label = "Date of Birth"        
        self.fields['marital_status'].label = "Marital Status"
        self.fields['blood_group'].label = "Blood Group"
        self.fields['covid19_vax_status'].label = "COVID-19 Vaccination Status"
        self.fields['contact_number'].label = "Contact Number"
        self.fields['annual_income'].label = "Annual Income"
        self.fields['earning_source'].label = "Earning Source"
        self.fields['annual_expenditure'].label = "Annual Expenditure"
        self.fields['academic_info'].label = "Academic Information"
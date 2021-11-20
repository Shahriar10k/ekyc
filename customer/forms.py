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
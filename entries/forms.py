from django.forms import ModelForm
from .models import *
from django import forms


class Student_info_form(ModelForm):
    class Meta:
        model = Student_info
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(Student_info_form, self).__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs.update({'class': 'btn btn-outline-secondary '})
    

class Personal_info_form(ModelForm):
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    VAX_STATUS = (
        ('Vaccinated', 'Vaccinated'),
        ('Unvaccinated', 'Unvaccinated'),
    )
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect, initial = 'Male')
    covid19_vax_status = forms.ChoiceField(choices=VAX_STATUS, widget=forms.RadioSelect)
    class Meta:
        model = Personal_info
        fields = [
            'id',
            'father_name',
            'mother_name',
            'gender',
            'date_of_birth',
            'religion',
            'citizenship',
            'marital_status',
            'blood_group',
            'covid19_vax_status',
            'address',
            'contact_number',
        ]

    def __init__(self, *args, **kwargs):
        super(Personal_info_form, self).__init__(*args, **kwargs)
                
        self.fields['id'].label = "Student's ID"
        self.fields['father_name'].label = "Father's name"
        self.fields['mother_name'].label = "Mother's name"
        self.fields['date_of_birth'].label = "Date of birth (YYYY-MM-DD):"
        self.fields['covid19_vax_status'].label = "COVID-19 Vaccination Status"

    
class Ssc_equivlent_form(ModelForm):
    class Meta:
        model = Ssc_equivlent
        fields = '__all__'
        

class Hsc_equivlent_form(ModelForm):
    class Meta:
        model = Hsc_equivlent
        fields = '__all__'
    

class Course_form(ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

class Grade_form(ModelForm):

    class Meta:
        model = Grade
        fields = '__all__'

class Financial_info_form(ModelForm):
    class Meta:
        model = Financial_info
        fields = '__all__'
    
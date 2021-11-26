from django.forms import ModelForm, widgets
from .models import *
from django import forms


class Student_info_form(ModelForm):
    class Meta:
        model = Student_info
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(Student_info_form, self).__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs.update({'class': 'btn btn-outline-secondary '})
    
        self.fields['nsu_id'].label = "Student ID"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['dept'].label = "Department"

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
                
        self.fields['father_name'].label = "Father's name"
        self.fields['mother_name'].label = "Mother's name"
        self.fields['date_of_birth'].label = "Date of birth (YYYY-MM-DD):"
        self.fields['covid19_vax_status'].label = "COVID-19 Vaccination Status"

    
class Ssc_equivlent_form(ModelForm):
    class Meta:
        model = Ssc_equivlent
        fields = [
            'school_name',
            'session',
            'passing_year',
            'gpa',
            'medium',
            'board',
            'id'
        ]

    def __init__(self, *args, **kwargs):
        super(Ssc_equivlent_form, self).__init__(*args, **kwargs)
                
        self.fields['id'].label = "Student ID"
        self.fields['school_name'].label = "School Name"
        self.fields['passing_year'].label = "Passing Year"
        self.fields['gpa'].label = "GPA"
        

class Hsc_equivlent_form(ModelForm):
    class Meta:
        model = Hsc_equivlent
        fields = [
            'college_name',
            'session',
            'passing_year',
            'gpa',
            'medium',
            'board',
            'id'
        ]

    def __init__(self, *args, **kwargs):
        super(Hsc_equivlent_form, self).__init__(*args, **kwargs)
                
        self.fields['id'].label = "Student ID"
        self.fields['college_name'].label = "College Name"
        self.fields['passing_year'].label = "Passing Year"
        self.fields['gpa'].label = "GPA"
    

class Course_form(ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super(Course_form, self).__init__(*args, **kwargs)

        self.fields['couse_code'].label = "Code"
        self.fields['course_title'].label = "Title"
        self.fields['course_desc'].label = "Description"
        self.fields['course_credit'].label = "Credit"

class Grade_form(ModelForm):

    class Meta:
        model = Grade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Grade_form, self).__init__(*args, **kwargs)

        self.fields['id'].label = "Student ID"
        self.fields['course_code'].label = "Course Code"
    

    id = forms.ModelChoiceField(
        queryset = Student_info.objects.all().order_by('nsu_id'),
    )
    course_code = forms.ModelChoiceField(
        queryset = Course.objects.all().order_by('couse_code'),
        widget = forms.TextInput()
    )

class Financial_info_form(ModelForm):
    class Meta:
        model = Financial_info
        fields = '__all__'
    
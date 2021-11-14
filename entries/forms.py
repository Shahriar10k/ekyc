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
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('OTHER','OTHER'),
    )
    VOTE_TYPE = (
        ('Taken', 'Taken'),
        ('Not taken', 'Not taken'),
    )
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect, initial = 'MALE')
    Covid19_status = forms.ChoiceField(choices=VOTE_TYPE, widget=forms.RadioSelect)
    class Meta:
        model = Personal_info
        fields = '__all__'

    
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

class Financial_history_form(ModelForm):
    class Meta:
        model = Financial_history
        fields = '__all__'
    
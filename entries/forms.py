from django.forms import ModelForm
from .models import *


class Student_info_form(ModelForm):
    class Meta:
        model = Student_info
        fields = '__all__'
          

class Personal_info_form(ModelForm):
    class Meta:
        model = Personal_info
        fields = '__all__'
        exclude = ['nsu_id']

class Ssc_equivlent_form(ModelForm):
    class Meta:
        model = Ssc_equivlent
        fields = '__all__'
        exclude = ['nsu_id']

class Hsc_equivlent_form(ModelForm):
    class Meta:
        model = Hsc_equivlent
        fields = '__all__'
        exclude = ['nsu_id']

class Semester_history_form(ModelForm):
    class Meta:
        model = Semester_history
        fields = '__all__'
        exclude = ['nsu_id']

class Financial_history_form(ModelForm):
    class Meta:
        model = Financial_history
        fields = '__all__'
        exclude = ['nsu_id']
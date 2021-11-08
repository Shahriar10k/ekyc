from django.db import models
import uuid
from django.db.models.indexes import Index
from autoslug import AutoSlugField

# Create your models here.

class Student_info(models.Model):
    nsu_id = models.CharField(max_length=100, unique=True, primary_key=True,)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    new_slug = AutoSlugField(populate_from='nsu_id', null=True, default=None)

    def __str__(self):
        return self.nsu_id

class Personal_info(models.Model):

    VOTE_TYPE = (
        ('taken', 'taken'),
        ('not taken', 'not taken'),
        ('registered', 'registered'),
        ('not registered', 'not registered'),
    )
    
    BLOOD_TYPE = (
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB-', 'AB-'),
    )

    MARITAL_STATUS = (
        ('MARRIED','MARRIED'),
        ('SINGLE','SINGLE'),
        ('DIVORCE','DIVORCE'),
        ('COMPLICATED','COMPLICATED'),
    )

    GENDER = (
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('OTHER','OTHER'),
    )

    nsu_id = models.ForeignKey(Student_info, on_delete=models.CASCADE, null=True, blank=True)
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,choices=GENDER)
    date_of_birth = models.DateField()
    address = models.TextField(max_length=100)
    religion = models.CharField(max_length=10)
    citizenship = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=100,choices=MARITAL_STATUS)
    blood_group = models.CharField(max_length=10,choices=BLOOD_TYPE)
    covid19_status = models.CharField(max_length=50, choices=VOTE_TYPE)
    contact_number = models.CharField(max_length=20)
    news_slug = AutoSlugField(populate_from='nsu_id',  null=True, default=None)



class Ssc_equivlent(models.Model):
    
    nsu_id = models.ForeignKey(Student_info, on_delete=models.CASCADE, null=True, blank=True)
    school_name = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    passing_year = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3 , decimal_places=2)
    medium = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    newd_slug = AutoSlugField(populate_from='nsu_id',  null=True, default=None)


class Hsc_equivlent(models.Model):
    
    nsu_id = models.ForeignKey(Student_info, on_delete=models.CASCADE, null=True, blank=True)
    collage_name = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    passing_year = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3 , decimal_places=2)
    medium = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    newf_slug = AutoSlugField(populate_from='nsu_id',  null=True, default=None)

class Semester_history(models.Model):

    SEMESTER_NAME = (
        ('SUMMER','SUMMER'),
        ('FALL','FALL'),
        ('SPRING','SPRING'),
    )

    nsu_id = models.ForeignKey(Student_info, on_delete=models.CASCADE, null=True, blank=True)
    semester_name= models.CharField(max_length=100,choices=SEMESTER_NAME)
    semester_year = models.DateField()
    semester_gpa = models.DecimalField(max_digits=3 , decimal_places=2)
    semester_cedit = models.CharField(max_length=100)
    newg_slug = AutoSlugField(populate_from='nsu_id', null=True, default=None)


class Financial_history(models.Model):
    
    nsu_id = models.ForeignKey(Student_info, on_delete=models.CASCADE, null=True, blank=True)
    annual_income = models.CharField(max_length=100)
    No_of_earning_person = models.IntegerField(null=True, blank=True)
    earning_source = models.CharField(max_length=100)
    annual_expenditure = models.IntegerField(null=True, blank=True)
    newh_slug = AutoSlugField(populate_from='nsu_id', null=True, default=None)
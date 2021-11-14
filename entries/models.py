from functools import partialmethod
from django.db import models
import uuid
from django.db.models.indexes import Index
from datetime import datetime, time
from autoslug import AutoSlugField

# Create your models here.

class Student_info(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nsu_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    

    def __str__(self):
        return self.nsu_id

class Personal_info(models.Model):

    VOTE_TYPE = (
        ('Taken', 'Taken'),
        ('Not taken', 'Not taken'),
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
        ('UNMARRIED','UNMARRIED'),    
    )

    GENDER = (
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('OTHER','OTHER'),
    )
    id = models.OneToOneField(Student_info, on_delete= models.CASCADE, primary_key=True)
    fathers_name = models.CharField(max_length=100, blank= True, null=True)
    mothers_name = models.CharField(max_length=100, blank= True, null=True)
    gender = models.CharField(max_length=20,choices=GENDER, blank= True, null=True)
    date_of_birth = models.DateField(blank= True, null=True)
    address = models.TextField(max_length=100,blank= True, null=True)
    religion = models.CharField(max_length=10,blank= True, null=True)
    citizenship = models.CharField(max_length=10,blank= True, null=True)
    marital_status = models.CharField(max_length=20,choices=MARITAL_STATUS,blank= True, null=True)
    blood_group = models.CharField(max_length=20,choices=BLOOD_TYPE,blank= True, null=True)
    covid19_status = models.CharField(max_length=20, choices=VOTE_TYPE,blank= True, null=True)
    contact_number = models.CharField(max_length=20,blank= True, null=True)
    



class Ssc_equivlent(models.Model):
    id = models.OneToOneField(Student_info, on_delete= models.CASCADE, primary_key=True)
    school_name = models.CharField(max_length=100, blank= True, null=True)
    session = models.IntegerField(blank= True, null=True)
    passing_year = models.IntegerField(blank= True, null=True)
    gpa = models.DecimalField(max_digits=3 , decimal_places=2, blank= True, null=True)
    medium = models.CharField(max_length=100, blank= True, null=True)
    board = models.CharField(max_length=100, blank= True, null=True)
    


class Hsc_equivlent(models.Model):
    
    id = models.OneToOneField(Student_info, on_delete= models.CASCADE, primary_key=True)
    collage_name = models.CharField(max_length=100,blank= True, null=True)
    session = models.IntegerField(blank= True, null=True)
    passing_year = models.IntegerField(blank= True, null=True)
    gpa = models.DecimalField(max_digits=3 , decimal_places=2, blank= True, null=True)
    medium = models.CharField(max_length=100, blank= True, null=True)
    board = models.CharField(max_length=100, blank= True, null=True)

class Course(models.Model):

    couse_code = models.CharField(primary_key=True, max_length=20, unique=True)
    course_title = models.CharField(max_length=100, blank= True, null=True)
    course_desc = models.TextField(max_length=100, blank= True, null=True)
    course_credit = models.IntegerField()  

class Grade(models.Model):

    SEMESTER_NAME = (
        ('SUMMER','SUMMER'),
        ('FALL','FALL'),
        ('SPRING','SPRING'),
    )

    GRADE_CHOICE = (
        ('A','A'),
        ('A-','A-'),
        ('B+','B+'),
        ('B','B'),
        ('B-','B-'),
        ('C+','C+'),
        ('C','C'),
        ('C-','C-'),
        ('D+','D+'),
        ('D','D'),
        ('F','F'),
        ('I','I'),
        ('W','W'),
    )
    id = models.ForeignKey(Student_info, on_delete= models.CASCADE, primary_key=True, unique=False)
    course_code = models.OneToOneField(Course, on_delete= models.CASCADE, blank= True, null=True)
    semester = models.CharField(max_length=20,choices=SEMESTER_NAME, blank= True, null=True)
    year = models.IntegerField(blank= True, null=True)
    grade = models.CharField(max_length=10,choices=GRADE_CHOICE, blank= True, null=True)


    


class Financial_history(models.Model):
    id = models.OneToOneField(Student_info, on_delete= models.CASCADE, primary_key=True)
    annual_income = models.IntegerField(blank= True, null=True)
    earning_source = models.CharField(max_length=100, blank= True, null=True)
    annual_expenditure = models.IntegerField(default=0, blank= True, null=True)
    
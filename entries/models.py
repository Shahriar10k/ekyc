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
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20,choices=GENDER)
    date_of_birth = models.DateField()
    address = models.TextField(max_length=100)
    religion = models.CharField(max_length=10)
    citizenship = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=20,choices=MARITAL_STATUS)
    blood_group = models.CharField(max_length=20,choices=BLOOD_TYPE)
    covid19_status = models.CharField(max_length=20, choices=VOTE_TYPE)
    contact_number = models.CharField(max_length=20)
    



class Ssc_equivlent(models.Model):
    id = models.OneToOneField(Student_info, on_delete= models.CASCADE, primary_key=True)
    school_name = models.CharField(max_length=100)
    session = models.IntegerField()
    passing_year = models.IntegerField()
    gpa = models.DecimalField(max_digits=3 , decimal_places=2)
    medium = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    


class Hsc_equivlent(models.Model):
    
    id = models.OneToOneField(Student_info, on_delete= models.CASCADE, primary_key=True)
    collage_name = models.CharField(max_length=100)
    session = models.IntegerField()
    passing_year = models.IntegerField()
    gpa = models.DecimalField(max_digits=3 , decimal_places=2)
    medium = models.CharField(max_length=100)
    board = models.CharField(max_length=100)

class Course(models.Model):

    couse_code = models.CharField(primary_key=True, max_length=20, unique=True)
    course_title = models.CharField(max_length=100)
    course_desc = models.TextField(max_length=100)
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
    course_code = models.OneToOneField(Course, on_delete= models.CASCADE)
    semester = models.CharField(max_length=20,choices=SEMESTER_NAME)
    year = models.IntegerField()
    grade = models.CharField(max_length=10,choices=GRADE_CHOICE)


    


class Financial_history(models.Model):
    id = models.OneToOneField(Student_info, on_delete= models.CASCADE, primary_key=True)
    annual_income = models.IntegerField()
    earning_source = models.CharField(max_length=100)
    annual_expenditure = models.IntegerField(default=0,blank=True)
    
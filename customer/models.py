from functools import partialmethod
from django.db import models
import uuid
from django.db.models.indexes import Index
from datetime import datetime, time
from django.core.validators import *

class Customer_info(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField("Customer Name",max_length=500)
    bin = models.CharField("Customer Business Identification Number(BIN)",max_length=9, validators=[MinLengthValidator(9)])
    email = models.EmailField("Customer Email", max_length=254)
    file = models.FileField("Scanned Picture/File", upload_to="files/%Y/%m/%d", blank=True, null=True)

class Customer_access_info(models.Model):
    customer_id = models.OneToOneField(Customer_info, on_delete=models.CASCADE)
    nsu_ID = models.BooleanField(default=False)
    first_name = models.BooleanField(default=False)
    last_name = models.BooleanField(default=False)
    department = models.BooleanField(default=False)
    program = models.BooleanField(default=False)
    batch = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    photo = models.BooleanField(default=False)
    father_name = models.BooleanField(default=False)
    mother_name = models.BooleanField(default=False)
    gender = models.BooleanField(default=False)
    data_of_birth = models.BooleanField(default=False)
    address = models.BooleanField(default=False)
    religion = models.BooleanField(default=False)
    citizenship = models.BooleanField(default=False)
    marital_status = models.BooleanField(default=False)
    blood_group = models.BooleanField(default=False)
    covid19_vax_status = models.BooleanField(default=False)
    contact_number = models.BooleanField(default=False)
    annual_income = models.BooleanField(default=False)
    earning_source = models.BooleanField(default=False)
    annual_expenditure = models.BooleanField(default=False)
    academic_info = models.BooleanField(default=False)


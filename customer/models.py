from functools import partialmethod
from django.db import models
import uuid
from django.db.models.indexes import Index
from datetime import datetime, time
from django.core.validators import *

class Customer_info(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField("Customer Name",max_length=500)
    bin = models.IntegerField("Customer Business Identification Number(BIN)", validators=[MinLengthValidator(9)])
    email = models.EmailField("Customer Email", max_length=254)
    file = models.FileField("Scanned Picture/File", upload_to="files/%Y/%m/%d", blank=True, null=True)


from django import template

register = template.Library()

from entries.models import Student_info
from customer.models import Customer_info

@register.simple_tag
def total_students():
    return Student_info.objects.all().count()

@register.simple_tag
def total_customers():
    return Customer_info.objects.all().count()
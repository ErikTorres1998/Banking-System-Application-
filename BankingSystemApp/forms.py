from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['balance'] # grab all fields from employee

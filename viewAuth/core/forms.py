from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import modelform_factory, ModelForm
from django.contrib.auth.models import User
from .models import *


class EmployeeForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

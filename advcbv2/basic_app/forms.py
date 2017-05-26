from django import forms
from django.contrib.auth.models import User
from basic_app.models import Employee
from django.db import models

class EmployeeCreateViewModel(forms.ModelForm):
    class Meta():
        model = Employee
        fields = ("name","position","education","email","age","telephone","loginatten","depname","profile_picture")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'})
        }

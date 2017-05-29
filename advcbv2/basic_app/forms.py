from django import forms
from django.contrib.auth.models import User
from basic_app.models import Employee
from django.db import models

class EmployeeCreateViewModel(forms.ModelForm):
    class Meta():
        model = Employee
        fields = ("name","education","position","email","age","salary","telephone","loginatten","depname","profile_picture")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass','placeholder': 'Name' }),
            'age': forms.NumberInput(attrs={'class': 'textinputclass','placeholder': 'Age' }),
            'email': forms.EmailInput(attrs={'class': 'textinputclass','placeholder': 'Email' }),
            'education': forms.TextInput(attrs={'class': 'textinputclass','placeholder': 'Position' }),
            'salary': forms.NumberInput(attrs={'class': 'textinputclass','placeholder': 'Salary' }),
            'position': forms.TextInput(attrs={'class': 'textinputclass','placeholder': 'Education' }),
            'depname': forms.MultipleHiddenInput(attrs={'class': 'textinputclass','placeholder': 'Education' }),
            'profile_picture': forms.FileInput(attrs={'class': 'fileinputclass' }),


        }

from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Select, ClearableFileInput
from basic_app.models import Employee
from django.db import models
from . import models

class EmployeeCreateViewModel(forms.ModelForm):
    class Meta():
        model = Employee
        choiceList = models.Employee.positionarr
        position = forms.ChoiceField(label = 'Position:',choices = choiceList,widget=Select(attrs={'class':'form-control' ,'selected':"ceo"}))
        fields = ("name","education","position","email","age","salary","telephone","loginatten","depname","profile_picture")
        #position = forms.ChoiceField(label = 'Position:',choices = choiceList,widget=Select(attrs={'class':'form-control' ,'selected':"ceo"}))
        widgets = {
            'name': forms.TextInput(attrs={ 'class': 'form-control','placeholder': 'Name' }),
            'age': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Age' }),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email' }),
            'telephone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Telephone' }),

            'education': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Education' }),
            'salary': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Salary' }),

            'loginatten': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Loginatten' }),
            #'depname': forms.ModelChoiceField(queryset=Color.objects.all()attrs={'class': 'textinputclass','placeholder': 'Education' }),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control' }),


        }

    def __init__(self, *args, **kwargs):
        super(EmployeeCreateViewModel, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = None
        # following line needed to refresh widget copy of choice list
        # self.fields['position'].widget.choices = self.fields['position'].choices

from django.db import models
from django.core.urlresolvers import reverse
from PIL import Image

from datetime import datetime
from django.utils import timezone
import dateutil.parser


# Create your models here.



class Department(models.Model):

    dep = models.CharField(max_length=256)


    def __str__(self):
        return self.dep
    def get_absolute_url(self):
        return reverse("basic_app:list")

class Employee(models.Model):

    positionarr = (('manager','Manager'),('employee','Employee'))
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256,choices = positionarr,default="")
    age = models.CharField(max_length=256,null=True)
    education = models.CharField(max_length=256, null = True)
    salary = models.IntegerField(null = True)
    email = models.EmailField(max_length=70,blank=True)
    telephone = models.CharField(max_length=256)
    depname = models.ForeignKey(Department,null=True,default="",related_name='depatments',on_delete=models.SET_NULL,blank=True )
    profile_picture = models.ImageField(upload_to='profile_pics')
    loginatten = models.CharField(max_length=256, unique= True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})



class Attendance(models.Model):

    @property
    def is_late(self):
        return dateutil.parser.parse('08:00:00+07') > self.time

    time = models.DateTimeField(default=datetime.now, blank=True)

    attendance_pic = models.ImageField(upload_to='attendance_pics',null = True, blank=True)

    employee = models.ForeignKey(Employee, related_name='employees')

    def __str__(self):
        return self.employee.name
    def get_absolute_url(self):
        return reverse("basic_app:list")

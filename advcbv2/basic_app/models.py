from django.db import models
from django.core.urlresolvers import reverse
from PIL import Image

from datetime import datetime



# Create your models here.

class Department(models.Model):

    dep = models.CharField(max_length=256)
    namedep = models.CharField(max_length=256)

    def __str__(self):
        return self.dep
    def get_absolute_url(self):
        return reverse("basic_app:list")

class Employee(models.Model):

    positionarr = (('ceo','CEO'),('manager','Manager'),('worker','Worker'))
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    age = models.CharField(max_length=256,null=True)
    education = models.CharField(max_length=256,choices = positionarr)
    salary = models.IntegerField(default = 0)
    email = models.EmailField(max_length=70,blank=True)
    telephone = models.CharField(max_length=256)
    depname = models.ForeignKey(Department,null=True,related_name='depatments')
    profile_picture = models.ImageField(upload_to='profile_pics')
    loginatten = models.CharField(max_length=256, unique= True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})



class Attendance(models.Model):
    time = models.DateTimeField(default=datetime.now, blank=True)
    employee = models.ForeignKey(Employee, related_name='employees')
    attendance_pic = models.ImageField(upload_to='attendance_pics',null = True)

    

    def __str__(self):
        return self.employee.name
    def get_absolute_url(self):
        return reverse("basic_app:list")

from django.db import models
from django.core.urlresolvers import reverse
from PIL import Image
<<<<<<< Updated upstream


=======
from datetime import datetime
>>>>>>> Stashed changes


# Create your models here.

class Department(models.Model):
    dep = models.CharField(default = 'depa',max_length=256)

    def __str__(self):
        return self.dep


class Employee(models.Model):

    positionarr = (('ceo','CEO'),('manager','Manager'))
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
<<<<<<< Updated upstream
    education = models.CharField(max_length=256)
    email = models.EmailField(max_length=70,blank=True)
    telephone = models.CharField(max_length=256)
    profile_picture = models.ImageField(upload_to='profile_pics')




=======
    education = models.CharField(max_length=256,choices = positionarr)
    email = models.EmailField(max_length=70,blank=True)
    telephone = models.CharField(max_length=256)
    depname = models.ForeignKey(Department,null=True,related_name='depatments')
    profile_picture = models.ImageField(upload_to='profile_pics')


>>>>>>> Stashed changes
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})



class Attendance(models.Model):
    time = models.DateTimeField(default=datetime.now, blank=True)
    employee = models.ForeignKey(Employee,related_name='employees')

    def __str__(self):
        return self.employee.name
    def get_absolute_url(self):
        return reverse("basic_app:list")

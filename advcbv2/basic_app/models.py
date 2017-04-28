from django.db import models
from django.core.urlresolvers import reverse
from PIL import Image




# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    education = models.CharField(max_length=256)
    email = models.EmailField(max_length=70,blank=True)
    telephone = models.CharField(max_length=256)
    profile_picture = models.ImageField(upload_to='profile_pics')




    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})



class Attendance(models.Model):
    name = models.CharField(max_length=256)
    time = models.PositiveIntegerField()
    employee = models.ForeignKey(Employee,related_name='employees')

    def __str__(self):
        return self.name

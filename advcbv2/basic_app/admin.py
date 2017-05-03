from django.contrib import admin
from basic_app.models import Employee, Attendance, Department
# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Attendance)

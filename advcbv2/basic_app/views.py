from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator
from django.forms import TextInput
from basic_app.forms import EmployeeCreateViewModel
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AttendanceSerializer
from django.utils import timezone
from rest_framework.parsers import MultiPartParser, JSONParser
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

import base64
from django.core.files.base import ContentFile

# Create your views here.

# Original Function View:
#
# def index(request):
#     return render(request,'index.html')
#
#

# Pretty simple right?
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    model = models.Employee
    num_books=model.objects.all().count()


    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_books':num_books,},
    )


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'basic_app/signup.html', {'form': form})
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        model = models.Employee
        context  = super().get_context_data(**kwargs)
        context['injectme'] = model.objects.all().count()
        return context

class EmployeeListView(LoginRequiredMixin,ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'

    model = models.Employee
    paginate_by = 8
    # def get_total(self):
    #     pass

class DepartmentListView(LoginRequiredMixin,ListView):

    model = models.Department
    paginate_by =10
    template_name = 'basic_app/department_list.html'

    def get_context_data(self,**kwargs):
        # 1. Get list of all departments
        # 2. Query employees in each department
        # 3. Use sum function to get a sum value of employees salary in EACH department
        departmentModal = models.Department
        employeeModel = models.Employee
        departmentResults = departmentModal.objects.all()
        return_results = []
        for department in departmentResults :
            salary = 0
            num_emp = 0
            em = {}
            employees = employeeModel.objects.filter(depname=department.id)
            for employee in employees :
                num_emp +=1
                salary += employee.salary
            em['salary'] = salary
            em['name'] = department.dep
            em['id_dep']= department.id
            em['num_emp']= num_emp
            return_results.append(em)
        print(return_results)
        employeeResults = employeeModel.objects.filter(depname=departmentResults);
        print('getting department resultt')
        print(departmentResults);
        print('getting department employees resultt')
        print(employeeResults);
        context  = super().get_context_data(**kwargs)
        context['department_salary'] = return_results
        print(return_results)

        model = models.Employee
        results = model.objects.all()
        context['injectme'] = model.objects.values('depname').annotate(Sum('salary')).order_by('depname')
        print('getting results')
        print(results)
        return context
class EmployeeSearchListView(LoginRequiredMixin,ListView):

    context_object_name = 'searchde'



    template_name = 'basic_app/search_employee.html'
    model = models.Employee
    model2= models.Department

    def get_queryset(self):
        try:
            print(self.kwargs)
            print(self.request.GET)
            q = self.request.GET['q']
            p = self.request.GET['posit']
            print(p)

        except:
            q = ''
        if (q != '' and p == 'na'):
            print("hello")
            object_list = self.model.objects.filter(name__icontains = q)
            print(object_list)
        elif (q != '' and p == 'idd'):
            print("test2")
            object_list = self.model.objects.filter(id__icontains = q)
        elif (q != '' and p == 'depart'):
            print("test3")
            object_list = self.model2.objects.filter(dep__icontains = q)
        else:
            print("fuck")
            object_list = self.model.objects.all()
        return object_list

class EmployeeDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'employee_details'
    model = models.Employee
    template_name = 'basic_app/employee_detail.html'
    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        attendancemodal = models.Attendance
        attendanceResults = attendancemodal.objects.all()
        context['late_time'] = datetime.strptime('8:00', '%H:%M')
        # context=['late_time':,'checktime':]
        return context


class DepartmentDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'department_details'
    model = models.Department
    template_name = 'basic_app/department_detail.html'
    def get_context_data(self,**kwargs):
        # model = models.Employee
        # context  = super().get_context_data(**kwargs)
        #
        # context['injectme'] = model.objects.values('depname').annotate(Sum('salary'))
        # print(self.kwargs['pk'])
        # return context


        departmentModal = models.Department
        employeeModel = models.Employee
        departmentResults = departmentModal.objects.filter(pk = self.kwargs['pk'])
        return_results = []
        for department in departmentResults :
            salary = 0
            num_emp = 0
            em = {}
            employees = employeeModel.objects.filter(depname=department.id)
            for employee in employees :
                num_emp +=1
                salary += employee.salary
            em['salary'] = salary
            em['name'] = department.dep
            em['id_dep']= department.id
            em['num_emp']= num_emp
            return_results.append(em)
        print(return_results)
        employeeResults = employeeModel.objects.filter(depname=departmentResults);
        print('getting department resultt')
        print(departmentResults);
        print('getting department employees resultt')
        print(employeeResults);
        context  = super().get_context_data(**kwargs)
        context['department_salary'] = return_results
        print(return_results)

        model = models.Employee
        results = model.objects.all()
        context['injectme'] = model.objects.values('depname').annotate(Sum('salary')).order_by('depname')
        print('getting results')
        print(results)
        return context
class EmployeeCreateView(LoginRequiredMixin,CreateView):
    form_class= EmployeeCreateViewModel


    model = models.Employee
    template_name = 'basic_app/employee_form.html'



class EmployeeUpdateView(LoginRequiredMixin,UpdateView):
    fields = ("name","position","salary")
    model = models.Employee
    template_name = 'basic_app/employee_form.html'

class EmployeeDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Employee
    success_url = reverse_lazy("basic_app:list")


class DepartmentDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Department
    success_url = reverse_lazy("basic_app:dlist")

class AttendanceCreateView(LoginRequiredMixin,CreateView):
    fields = ("employee","time","attendance_pic")
    model = models.Attendance
    template_name = 'basic_app/employee_form.html'

class DepartmentCreateView(LoginRequiredMixin,CreateView):
    fields =("dep","namedep")
    model = models.Department
    template_name = 'basic_app/employee_form.html'



class AttendanceList(APIView):

    queryset = models.Attendance.objects.all()
    # serializer_class = AttendanceSerializer
    # parser_classes = (MultiPartParser, JSONParser)
    def get(self,request):
        model = models.Attendance
        attendances = model.objects.all()
        serializer = AttendanceSerializer(attendances, many = True)
        return Response(serializer.data)

    def post(self,request,format=None):

        now = timezone.now()
        # print(request.data)
        serializer = AttendanceSerializer(data=request.data)
        print('test')
        print(serializer)
        # serializer.is_valid(raise_exception=True)
        print("before check is valid")
        # print(serializer.attendance_pic)

        if serializer.is_valid():
            serializer.save(time=now)
            print('check is valid')
            # emp = serializer.validated_data.get("employee")
            # obj = models.Attendance.objects.create(time=now, employee=emp)
            return Response("Success", status=status.HTTP_201_CREATED)
            # return Response(AttendanceSerializer(obj).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')

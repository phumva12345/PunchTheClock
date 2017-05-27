from django.shortcuts import render
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
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        model = models.Employee
        context  = super().get_context_data(**kwargs)
        context['injectme'] = model.objects.all().count()
        return context

class EmployeeListView(ListView):
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

class DepartmentListView(ListView):

    model = models.Department
    paginate_by =10
    template_name = 'basic_app/department_list.html'
    def get_context_data(self,**kwargs):
        model = models.Employee
        context  = super().get_context_data(**kwargs)

        context['injectme'] = model.objects.values('name', 'depname').annotate(Sum('salary'))

        return context
class EmployeeSearchListView(ListView):

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

class EmployeeDetailView(DetailView):
    context_object_name = 'employee_details'
    model = models.Employee
    template_name = 'basic_app/employee_detail.html'


class DepartmentDetailView(DetailView):
    context_object_name = 'department_details'
    model = models.Department
    template_name = 'basic_app/department_detail.html'
    def get_context_data(self,**kwargs):
        model = models.Employee
        context  = super().get_context_data(**kwargs)

        context['injectme'] = model.objects.values('depname').annotate(Sum('salary'))

        return context
class EmployeeCreateView(CreateView):
    form_class= EmployeeCreateViewModel


    model = models.Employee
    template_name = 'basic_app/employee_form.html'



class EmployeeUpdateView(UpdateView):
    fields = ("name","position","salary")
    model = models.Employee
    template_name = 'basic_app/employee_form.html'

class EmployeeDeleteView(DeleteView):
    model = models.Employee
    success_url = reverse_lazy("basic_app:list")

class AttendanceCreateView(CreateView):
    fields = ("employee","time")
    model = models.Attendance
    template_name = 'basic_app/employee_form.html'

class DepartmentCreateView(CreateView):
    fields =("dep","namedep")
    model = models.Department
    template_name = 'basic_app/employee_form.html'

class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')

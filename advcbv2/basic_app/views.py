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

# Create your views here.

# Original Function View:
#
# def index(request):
#     return render(request,'index.html')
#
#

# Pretty simple right?
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context

class EmployeeListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'

    model = models.Employee
    paginate_by = 10

class EmployeeSearchListView(ListView):
<<<<<<< Updated upstream


    context_object_name = 'searchde'

=======


    context_object_name = 'searchde'

>>>>>>> Stashed changes
    template_name = 'basic_app/search_employee.html'
    model = models.Employee

    def get_queryset(self):
        try:
            print(self.kwargs)
            print(self.request.GET)
            q = self.request.GET['q']
<<<<<<< Updated upstream

        except:
            q = ''
        if (q != ''):
            object_list = self.model.objects.filter(name__icontains = q)
        else:
=======
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
            print("Fuck you")
            object_list = self.model.objects.filter(id__icontains = q)
        else:
            print("fuck")
>>>>>>> Stashed changes
            object_list = self.model.objects.all()
        return object_list

class EmployeeDetailView(DetailView):
    context_object_name = 'employee_details'
    model = models.Employee
    template_name = 'basic_app/employee_detail.html'


class EmployeeCreateView(CreateView):
<<<<<<< Updated upstream
    fields = ("name","position","education","email","telephone","profile_picture")
=======
    fields = ("name","position","education","email","telephone","depname","profile_picture")
>>>>>>> Stashed changes
    model = models.Employee
    template_name = 'basic_app/employee_form.html'


class EmployeeUpdateView(UpdateView):
    fields = ("name","position")
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
    fields =("dep")
    model = models.Department
    template_name = 'basic_app/employee_form.html'

class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')

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


    context_object_name = 'searchde'

    template_name = 'basic_app/search_employee.html'
    model = models.Employee

    def get_queryset(self):
        try:
            print(self.kwargs)
            print(self.request.GET)
            q = self.request.GET['q']

        except:
            q = ''
        if (q != ''):
            object_list = self.model.objects.filter(name__icontains = q)
        else:
            object_list = self.model.objects.all()
        return object_list

class EmployeeDetailView(DetailView):
    context_object_name = 'employee_details'
    model = models.Employee
    template_name = 'basic_app/employee_detail.html'


class EmployeeCreateView(CreateView):
    fields = ("name","position","education","email","telephone","profile_picture")
    model = models.Employee
    template_name = 'basic_app/employee_form.html'


class EmployeeUpdateView(UpdateView):
    fields = ("name","position")
    model = models.Employee
    template_name = 'basic_app/employee_form.html'

class EmployeeDeleteView(DeleteView):
    model = models.Employee
    success_url = reverse_lazy("basic_app:list")


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')

from turtle import position
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Department, Employee, Position
from .forms import DepartmentForm, EmployeeForm, PositionForm
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from my_app import forms


def welcome(request):
    return HttpResponse("Welcome to our company")

def search_form(request):
    return render(request, 'search_form.html')

def emp_view(request):
    employees = Employee.objects.all()
    return render(request, 'emp_list.html', {'employees': employees})

def dep_view(request):
    departments = Department.objects.all()
    return render(request, 'dep_list.html', {'departments': departments})

def search(request):
    employee_name = request.GET.get('first_last_name')
    employee = Employee.objects.filter(first_last_name__icontains=employee_name)
    return HttpResponse(employee)

def filter_employees(request, pk):
    employees = Employee.objects.filter(department__id = pk)
    return render(request, 'emp_list.html', {'employees': employees})


class Create(CreateView):
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return(redirect(reverse('all_employees')))

class EmployeeCreate(Create):
    form_class = EmployeeForm
    template_name = 'employee_form.html'

class PositionCreate(Create):
    form_class = PositionForm
    template_name = 'position_form.html'

class DepartmentCreate(Create):
    form_class = DepartmentForm
    template_name = 'department_form.html'

class AllEmployees(ListView):
    model = Employee
    template_name = 'emp_list.html'
    context_object_name = 'employees'

class AllDeps(ListView):
    model = Department
    #queryset = Department.objects.all()[:2]
    template_name = 'dep_list.html'
    context_object_name = 'departments'

class EmpDetail(DetailView):
    model = Employee
    template_name = 'single_emp.html'
    context_object_name = 'single_emp'

class EmpDelete(DeleteView):
    model = Employee
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('all_employees')

class EmpUpdate(UpdateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = '__all__'

class DepDetail(DetailView):
    model = Department
    template_name = 'single_dep.html'
    context_object_name = 'single_dep'

class DepDelete(DeleteView):
    model = Department
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('all_depatments')

class DepUpdate(UpdateView):
    model = Department
    template_name = 'department_form.html'
    fields = '__all__'
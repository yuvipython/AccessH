from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Department, Employee


class DepartmentListView(ListView):
    model = Department


class DepartmentDetailView(DetailView):
    model = Department


class EmployeeListView(ListView):
    model = Employee


def employee(request):
    if request.method == 'POST':

        name = request.POST.get('name', '')
        dept = request.POST.get('dept', '')

        emp = Employee(Employee_name=name, Department=dept)
        emp.save()

        return render(request, 'staff/employee.html', {'thank': 'thank you', 'id': id})
    return render(request, 'staff/employee.html')

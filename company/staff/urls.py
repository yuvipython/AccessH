__author__ = "Yuvi"

from django.urls import path

# importing views from views..py
from . import views
from .views import DepartmentListView, DepartmentDetailView, EmployeeListView

urlpatterns = [
    path('emplist/', EmployeeListView.as_view()),
    path('deptlist/', DepartmentListView.as_view()),
    path('deptdetails/<pk>', DepartmentDetailView.as_view()),
    path("employee/", views.employee, name="employee"),

]


from django.db import models


class Employee(models.Model):
    Employee_name = models.CharField(max_length=60)
    Department = models.CharField(max_length=50)
    Email = models.EmailField(max_length=30)
    Date_of_birth = models.DateField(null=True)
    Picture = models.ImageField(upload_to='staff/images', default='')

    def __str__(self):
        return self.Employee_name

    class Meta:
        db_table = 'Employee'


class Department(models.Model):
    Department_name = models.CharField(max_length=60)
    Manager = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Department_name

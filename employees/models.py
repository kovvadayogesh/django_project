from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class EmployeeDetails(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    departmet = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.employee.name
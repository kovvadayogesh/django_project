from django.contrib import admin
from .models import Employee, EmployeeDetails
# Register your models here.


class AdminEmployee(admin.ModelAdmin):
    list_display=('name','email','phone')
    search_field = ('name','email','phone')

class AdminEmployeeDetails(admin.ModelAdmin):
    list_display = ('employee','address','departmet','salary')
    search_field = ('employee','address','departmet','salary')

admin.site.register(Employee,AdminEmployee)
admin.site.register(EmployeeDetails,AdminEmployeeDetails)

from django.contrib import admin
from .models import Student
# Register your models here.


class StudentAmin(admin.ModelAdmin):
    list_display = ('name','email','phone','address')
    search_field = ('name','email','phone','address')


admin.site.register(Student,StudentAmin)
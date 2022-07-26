from django.contrib import admin

# Register your models here.
from demoapp.models import Employee

@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','dob','address','gender','state']

from django.contrib import admin

# Register your models here.
from demoapp.models import Employee ,Items, AssignedItem

admin.site.register(Employee)
# class EmployeeModelAdmin(admin.ModelAdmin):
#     list_display = ['id','name','email','dob','address','gender','state']
admin.site.register(Items)
admin.site.register(AssignedItem)


from django.contrib import admin
from .models import Employees, AvailableJobs








@admin.register(Employees)

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email_id','phone_number','gender']


# Register your models here.
@admin.register(AvailableJobs)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['name']




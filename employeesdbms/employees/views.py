from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees

# Create your views here.
def home(request):
    #return HttpResponse('This function will render Home Page')
    employees_details = Employees.objects.all()
    context = {
        'employee_details':employees_details
    }
    return render(request, 'home.html', context)

def details(request, id):
    #return HttpResponse('This page will show the Details based on ID {}'.format(id))
    employee_id = Employees.objects.get(id=id)
    context_id = {
        'employee':employee_id
    }

    return render(request, 'details.html', context_id)
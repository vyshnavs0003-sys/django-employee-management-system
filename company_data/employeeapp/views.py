from django.shortcuts import redirect, render
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def home(request):
    employees = Employee.objects.all()
    return render(request,'home.html',{'employees':employees})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request,'add_employee.html',{'form':form})  

def update_employee(request, emp_id):
    employee = Employee.objects.get(id=emp_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)
    return render(request,'update_empployee.html',{'form':form})

def delete_employee(request, emp_id):
    employee = Employee.objects.get(id=emp_id)
    employee.delete()
    return redirect('home')              
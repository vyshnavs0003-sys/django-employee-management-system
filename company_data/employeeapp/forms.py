from django import forms

from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields =['department','employee_name','email','phone','salary','joining_date']
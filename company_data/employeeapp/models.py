
from django.db import models

# Create your models here.
class Department(models.Model):
    department_name =models.CharField(max_length=100)
    department_head =models.CharField(max_length=100)
    location =models.CharField(max_length=100)

class Employee(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)    
    employee_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone =models.CharField(max_length=10)
    salary =models.IntegerField()
    joining_date=models.DateField()

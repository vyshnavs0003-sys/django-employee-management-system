from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('add/',views.add_employee,name='add_employee'),
    path('update/<int:emp_id>',views.update_employee,name='update_employee'),
    path('delete/<int:emp_id>',views.delete_employee,name='delete_employee'),

   
]

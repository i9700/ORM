from django.contrib import admin
from django.urls import path
from student.views import add_student, select_student

urlpatterns = [

    path('add/', add_student),
    path('select/', select_student),
]

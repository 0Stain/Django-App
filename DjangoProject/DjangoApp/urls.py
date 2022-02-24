from unicodedata import name
from django.urls import path
from .views import homePage,StudentListView, student_list, student_details, coach_list

urlpatterns = [
    path('home/',homePage,name='home'),
    #path('students/',student_list,name='student_list'),
    path('coaches/',coach_list,name='coach_list'),
    path('liststudents/', StudentListView.as_view(), name='student_list1'),
    path('student/<int:id>',student_details,name='student_details'),
]
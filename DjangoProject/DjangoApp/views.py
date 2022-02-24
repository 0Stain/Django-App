from wsgiref.util import request_uri
from django.http import HttpResponse
from django.shortcuts import render
from DjangoApp.models import Coach, Student
from django.views.generic import ListView


# Create your views here.
def homePage(request):
    return render(
        request,
        'app/index.html',

    )

def student_details(request, id):
    student = Student.objects.get(id=id)
    return render(
        request,
        'app/st_details.html',
        {
            'student': student,
        }
    )

class StudentListView(ListView):
    model = Student
    template_name = "app/student_list.html"

def student_list(request):
    list = Student.objects.all()
    list_coachs = Coach.objects.all()

    return render(
        request,
        'app/student_list.html',
        {
            'students': list,
            'coachs': list_coachs,
        }
    )

def coach_list(request):

    list_coachs = Coach.objects.all()

    return render(
        request,
        'app/coach_list.html',
        {
            'coachs': list_coachs,
        }
    )
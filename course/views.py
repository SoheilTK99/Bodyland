from django.shortcuts import render
from .models import Course


def course_list(request):
    course_list = Course.objects.all()
    context = {
        'courses' : course_list
    }
    return render (request,"blog/home.html",context)




def course_detail(request,id):
    course_detail = Course.objects.get(id=id)
    context = {
        'courseid' : course_detail
    }
    return render (request,"course/course_detail.html",context)


from django.shortcuts import render
from .models import Post
from course.models import Course

def blog_list(request):
    blog_list = Post.objects.all().order_by('-created_at')
    course_list = Course.objects.all()
    context = {
        "posts" : blog_list,
        "courses": course_list
    }
    return render(request,"blog/home.html",context)

def blog_detail(request,id):
    post = Post.objects.get(id=id)
    context = {
        "post": post
    }
    return render(request,"blog/blog_detail.html",context)


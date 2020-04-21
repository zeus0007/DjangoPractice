from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone


def home(request):
    blogs = Blog.objects  # 쿼리셋 (모델로부터 전달 받은 객체) #기능들을 표시해주는 방법을 메소드 라고함.
    return render(request, 'home.html', {'blogs1': blogs})


def create(request):
    return render(request, 'create.html')


def edit(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'details': details})


def getData(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/')


def deleteData(request):
    deleteDataId = request.GET['id']
    deleteDataId = int(deleteDataId)
    blog = Blog.objects.get(id=deleteDataId)
    print(blog)
    blog.delete()
    return redirect('/')


def editData(request):
    updateDataId = request.GET['id']
    updateDataId = int(updateDataId)
    blog = Blog.objects.get(id=updateDataId)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/')

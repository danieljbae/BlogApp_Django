from django.shortcuts import render
from django.http import HttpResponse
from .models import Post # database table Post


# Views will always return: a HTTP Resonse or an exception
# Home page
def home(request):
    context = {
        'posts': Post.objects.all()  # pulling from database
    }
    return render(request, 'blog/home.html', context)  # passing data 'context' into template


# About page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

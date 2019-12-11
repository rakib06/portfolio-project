from django.shortcuts import render
from .models import Blog

def all_blog(request):
    blog = Blog.objects
    return render(request, 'blog/all_blog.html', {'blog': blog})

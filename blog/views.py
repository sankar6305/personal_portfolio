from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'all_blogs.html', {'blogs_posts' : blogs})

def detail(request, blog_id):
    blog1 = get_object_or_404(Blog, pk = blog_id)
    return render(request,'detail.html', {'blog' : blog1})
from django.shortcuts import render
from . models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects.filter(status='p')
    
    context = {
        'blogs': blogs
    }
    return render(request, 'home.html', context)


def detail(request, pk):
    blog = Blog.objects.get(pk=pk)

    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context)
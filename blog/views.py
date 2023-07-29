from django.shortcuts import render
from django.http import HttpResponse
from .models import blogPost

# Create your views here.


def index(request):
    data = blogPost.objects.all()
    for i in data:
        print(i.thumbnail)
    params = {"blogs": data}
    return render(request, 'blog/index.html', params)


def viewBlog(request, blogId):
    data2 = blogPost.objects.filter(blog_id=blogId)
    params = {"blog": data2}
    return render(request, 'blog/viewBlog.html', params)

from http.client import HTTPResponse
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import BlogPost
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, user_passes_test 
from website.forms import CreateArticle

# Create your views here.
def blog_posts(request):
    posts = BlogPost.objects.all()
    name = "<script>alert('Hello world')</script>"
    return render(request, "blog/index.html", context={"posts": posts, 'name':name})

def blog_post(request,slug):
    post = BlogPost.objects.get(pk=slug)
    return render(request, "blog/post.html", context={"post": post})

def homer(request):
    return render(request, "blog/base.html")

def signUp(request):
    return HttpResponse("Cree mon compte")
from http.client import HTTPResponse
# from django.http.response import Http404, HttpResponse
# from django.shortcuts import get_object_or_404, redirect, render
# from blog.models import BlogPost
# from django.template.loader import render_to_string
# from django.contrib.auth.decorators import login_required, user_passes_test 


# # Create your views here.
# def vieewwww(request):
#     r = HttpResponse()
#     r.content = "{ '1': 'Bonjour tout le monde' }"
#     r.status_code = 404
#     r['Content-Type'] = 'application/json'
#     return r

# # @user_passes_test(lambda u: u.username == "macbook")
# def  blog_post(request, slug):
#     blogs = BlogPost.objects.all()
#     blog_post= get_object_or_404(BlogPost, pk=slug)
#     for blog in blogs:
#         print(blog.title)
#     print(blogs)
#     return render(request, "blog/post.html", context={"posts": blogs})

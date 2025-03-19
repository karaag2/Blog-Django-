from django.shortcuts import HttpResponse, render

from website.forms import SignUpForm,CreateArticle

def home(request):
    return render(request, "home.html")
def signup(request):
    if request.method  =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        print(request.POST.get('cgu_accepted'))
    else:
        form = SignUpForm() 
    return render(request, "accounts/signup.html", {"form":form})
def blog_post(request,slug):
    post = BlogPost.objects.get(pk=slug)
    return render(request, "blog/post.html", context={"post": post})

def homer(request):
    return render(request, "blog/base.html")

def signUp(request):
    return HttpResponse("Cree mon compte")
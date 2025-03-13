from django.shortcuts import HttpResponse


def home(request):
    out = HttpResponse("<h1 style='color: red;'>Welcome to the homepage</h1>")
    return out
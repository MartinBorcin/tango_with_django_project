from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hey there partner! Go ahead and visit the <a href=/rango/about> about page </a>.")


def about(request):
    return HttpResponse("Rango says this is the about page. <br/> <a href=/> <- Go Back Home </a>")

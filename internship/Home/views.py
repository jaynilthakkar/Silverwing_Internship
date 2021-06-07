from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello Python")


def home(request):
    return render(request, 'index.html')

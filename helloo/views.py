from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(response):
    return HttpResponse("Hello, World!")
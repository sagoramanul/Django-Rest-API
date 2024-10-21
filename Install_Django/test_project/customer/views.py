from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def customer(requset):
    return HttpResponse("Hello world!")

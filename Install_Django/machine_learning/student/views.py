from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def stu(request):
    return HttpResponse('Welcome to Django Platform Sagor')
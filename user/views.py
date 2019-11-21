from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# a function to show User's homepage
def homepage(request):
    return HttpResponse('<h1>User App Homepage<h1>')


# a test function
def test(request):
    return HttpResponse('TEST RESPONSE')


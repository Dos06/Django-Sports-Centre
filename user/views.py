from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# a test function
def test(request):
    return HttpResponse('TEST RESPONSE')


# a function to show User's homepage
def index(request):
    return HttpResponse("<h1>User App Homepage<h1>")

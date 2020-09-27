from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')


def function1(request):
    return HttpResponse('this FUNCTION1')
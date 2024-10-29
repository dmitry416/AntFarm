from django.http import HttpResponse
from django.shortcuts import render

def auth(request):
    return HttpResponse('<h1>AUTH!!!</h1>')
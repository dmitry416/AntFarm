from django.http import HttpResponse
from django.shortcuts import render

def game(request):
    return HttpResponse('<h1>GAME!!!</h1>')
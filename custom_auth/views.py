from django.http import HttpResponse
from django.shortcuts import render

def auth(request):
    return render(request, 'custom_auth.html')
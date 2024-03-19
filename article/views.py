from django.shortcuts import render
from django.http import HttpResponse

def article(request):
    return HttpResponse('In the name of allah.')
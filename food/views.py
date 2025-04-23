from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def biriyani(request):
    return HttpResponse('Biriyani is Lub')
def beer(request):
    return HttpResponse('Beer is not good for health')

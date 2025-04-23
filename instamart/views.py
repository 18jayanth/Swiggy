from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Chocolates(request):
    return HttpResponse('Chocolates is tasty')
def Biscuits(request):
    return HttpResponse('Biscuits are crunchy')

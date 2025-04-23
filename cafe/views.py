from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def coffee(request):
    return HttpResponse('Capichino Coffee is excellent')
def tea(request):
    return HttpResponse('Try Ginger Tea good for health')

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def radha(request):
    return HttpResponse('radha is nice girl')
def demo(request):
    return HttpResponse('it is showing webpages')
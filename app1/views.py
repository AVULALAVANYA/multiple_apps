from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def krishna(request):
    return HttpResponse('<h1><marquee>krishna is a most powerfull person in this world<marquee></h1>')
def sumed(request):
    return HttpResponse('<h1><marquee>he is acting on radhakrishna serial and good actor also</h1></marquee>')
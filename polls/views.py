from django.shortcuts import render

# Create your views hefr

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,World. You are at the polls index.")
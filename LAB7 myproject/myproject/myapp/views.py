from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    return HttpResponse("ICT12367 SPU</h1>")
def about(request):
    return HttpResponse("<h1>About ICT12367 SPU</h1>")
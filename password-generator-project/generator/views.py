from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


# Create your views here.
def home(request):
    return render(request, "generator/home.html", {'password':'1234567788'})


def eggs(request):
    return HttpResponse(",h1>Eggs are so tasty</h1>")
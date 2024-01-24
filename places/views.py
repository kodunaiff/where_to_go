from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def show_places(request):
    return render(request, 'index.html')

# Create your views here.

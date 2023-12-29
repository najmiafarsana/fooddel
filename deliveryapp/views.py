from django.http import request
from django.template import loader
from django.shortcuts import render
from .models import food

# Create your views here.

def index(request):
    obj = food.objects.all()
    return render(request, "index.html",{'result':obj})




from django.shortcuts import render, HttpResponse

# step-0 -> go to models.py and for steps go readme.md

# Create your views here.
def home(request):
    return HttpResponse("hello")


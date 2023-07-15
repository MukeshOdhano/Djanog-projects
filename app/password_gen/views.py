from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random


# Create your views here.
def index(request):
    return render(request, "index.html")


def random_pass(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    password = ''
       
    if request.GET.get('uppercase'):
        char.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("digits"):
        char.extend(list('0123456789'))
    if request.GET.get('symbols'):
        char.extend(list('/.%&^()_-+='))
        
    # print(request.GET.get('length'))
    for c in range(int(request.GET.get('length'))):
        password += random.choice(char)
    
    return render(request, "password.html", {"passw": password})


# json
"""def pass_gen(request): # pas_gen(request)
    char = list('abcdefghijklmnopqrstuvwxyz')
       
    password = ''

    if request.GET.get('uppercase'):
        char.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        
    
    for c in range(15):
        password += random.choice(char)
    
    genrated_password = {'password' : password}
    return JsonResponse(genrated_password)  """

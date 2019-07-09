from django.shortcuts import render
from django.http import HttpResponse



from . import models

# Create your views here.
from django.http import HttpResponse

def hello(request):
    li = models.employee._meta.get_fields()
    ul = []
    print(li)
    for i in li:
        ul.append(str(i).split('.')[-1])
    text = "<h1>welcome to my app number %s!</h1>"
    return HttpResponse(ul)
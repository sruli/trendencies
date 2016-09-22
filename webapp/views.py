from django.shortcuts import render
from django.http import HttpResponse

def index_webapp(request):
    return HttpResponse("<h2>WEB-APP-NEW</h2>")

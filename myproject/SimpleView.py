from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("This is simple website")
def htmlpage(request):
    return render(request,'index.html')
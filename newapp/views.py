from django.shortcuts import render
from django.http import HttpResponse
def about(request):
    return render(request,'base.html')
def home(request):
    return render(request, 'home.html')
   

# Create your views here.

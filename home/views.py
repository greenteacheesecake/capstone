from django.shortcuts import render
from django.shortcuts import redirect

def home_view(request):
    return render(request, 'home.html')

def home1_view(request):
    return render(request, 'home1.html')

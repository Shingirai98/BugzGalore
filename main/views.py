from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    context = {'title':'Home'}
    return render(request, 'main/homepage.html', context)

def about(request):
    context = {'title':'About'}
    return render(request, 'main/about.html', context)
from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'front/home.html', context)

def login(request):
    context = {}
    return render(request, 'front/login.html', context)

def signup(request):
    context = {}
    return render(request, 'front/signup.html', context)

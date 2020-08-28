from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    return render(request, 'home.html')

def location(request):
    return render(request, 'location.html')

def write(request):
    return render(request, 'write.html')

def account(request):
    return render(request, 'account.html')

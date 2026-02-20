from django.shortcuts import render

def login_view(request):
    return render(request, 'users/login.html')

def register_view(request):
    return render(request, 'users/register.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')
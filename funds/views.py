




from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def fund_list(request):
    return render(request, 'funds/fund_list.html')

def compare(request):
    return render(request, 'funds/compare.html')

from django.shortcuts import render
from .models import Fund

def fund_list(request):
    funds = Fund.objects.all()
    return render(request, 'funds/fund_list.html', {'funds': funds})

def compare_funds(request):
    funds = Fund.objects.all()
    return render(request, 'funds/compare.html', {'funds': funds})


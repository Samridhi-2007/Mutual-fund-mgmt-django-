from django.shortcuts import render
from .models import Fund

def fund_list(request):
    funds = Fund.objects.all()
    return render(request, 'funds/fund_list.html', {'funds': funds})

def compare_funds(request):
    funds = Fund.objects.all()
    return render(request, 'funds/compare.html', {'funds': funds})
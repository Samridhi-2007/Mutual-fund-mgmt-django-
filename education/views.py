from django.shortcuts import render
from .models import Article

def education_page(request):
    articles = Article.objects.all()
    return render(request, 'education/education.html', {'articles': articles})
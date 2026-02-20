from django.urls import path
from . import views

urlpatterns = [
    path('', views.education_page, name='education'),
]
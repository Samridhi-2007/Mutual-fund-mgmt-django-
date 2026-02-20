from django.urls import path
from . import views

urlpatterns = [
    path('', views.fund_list, name='fund_list'),
    path('compare/', views.compare_funds, name='compare_funds'),
]
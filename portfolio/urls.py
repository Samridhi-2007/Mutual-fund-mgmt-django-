from django.urls import path

from . import views

urlpatterns = [
    path('my-investments/', views.my_investments, name='my_investments'),
    path('invest/<int:fund_id>/', views.invest_in_fund, name='invest_in_fund'),
]

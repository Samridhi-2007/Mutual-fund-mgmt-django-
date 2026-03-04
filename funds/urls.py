from django.urls import path

from . import views

urlpatterns = [
    path('', views.FundListView.as_view(), name='fund_list'),
    path('create/', views.FundCreateView.as_view(), name='fund_create'),
    path('risk-analysis/', views.risk_analysis, name='risk_analysis'),
    path('<int:pk>/', views.FundDetailView.as_view(), name='fund_detail'),
    path('<int:pk>/edit/', views.FundUpdateView.as_view(), name='fund_update'),
    path('<int:pk>/delete/', views.FundDeleteView.as_view(), name='fund_delete'),
    path('compare/', views.compare_funds, name='compare_funds'),
]

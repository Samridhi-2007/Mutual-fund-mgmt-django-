from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdvisorListView.as_view(), name='advisor_list'),
    path('create/', views.AdvisorCreateView.as_view(), name='advisor_create'),
    path('<int:pk>/', views.AdvisorDetailView.as_view(), name='advisor_detail'),
    path('<int:pk>/edit/', views.AdvisorUpdateView.as_view(), name='advisor_update'),
    path('<int:pk>/delete/', views.AdvisorDeleteView.as_view(), name='advisor_delete'),
]

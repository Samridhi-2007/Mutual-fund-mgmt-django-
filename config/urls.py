from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('funds.urls')),         # Home & funds
    path('users/', include('users.urls')),   # Login/Register/Dashboard
    path('education/', include('education.urls')),
]

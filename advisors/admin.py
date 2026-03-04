from django.contrib import admin

from .models import Advisor


@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'expertise', 'experience_years')
    search_fields = ('name', 'email', 'expertise')

from django.contrib import admin

from .models import Fund


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'risk_level', 'returns_1yr', 'returns_3yr')
    search_fields = ('name', 'category', 'risk_level')

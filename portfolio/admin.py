from django.contrib import admin

from .models import Investment


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'fund', 'amount', 'nav_price', 'units_purchased', 'invested_at')
    search_fields = ('user__username', 'fund__name')

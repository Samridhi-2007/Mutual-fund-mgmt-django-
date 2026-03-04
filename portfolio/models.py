from decimal import Decimal

from django.conf import settings
from django.db import models


class Investment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='investments')
    fund = models.ForeignKey('funds.Fund', on_delete=models.CASCADE, related_name='investments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    nav_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('100.00'))
    units_purchased = models.DecimalField(max_digits=12, decimal_places=4)
    invested_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-invested_at']

    def __str__(self):
        return f'{self.user.username} -> {self.fund.name} ({self.amount})'

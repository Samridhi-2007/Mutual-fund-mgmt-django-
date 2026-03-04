from decimal import Decimal

from django import forms


class InvestmentForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        min_value=Decimal('100.00'),
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
    )
    nav_price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=Decimal('0.01'),
        initial=Decimal('100.00'),
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        help_text='Enter current NAV price per unit.',
    )

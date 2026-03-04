from django import forms

from .models import Fund


class FundForm(forms.ModelForm):
    class Meta:
        model = Fund
        fields = [
            'name',
            'category',
            'risk_level',
            'expense_ratio',
            'returns_1yr',
            'returns_3yr',
        ]

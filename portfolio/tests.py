from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from education.models import Article
from funds.models import Fund
from .models import Investment


class InvestmentFlowTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.investor = user_model.objects.create_user(
            username='investor_flow',
            email='investor_flow@example.com',
            password='StrongPass123!',
            role='INVESTOR',
        )
        self.advisor = user_model.objects.create_user(
            username='advisor_flow',
            email='advisor_flow@example.com',
            password='StrongPass123!',
            role='ADVISOR',
        )
        self.fund = Fund.objects.create(
            name='Test Growth Fund',
            category='Equity',
            risk_level='High',
            expense_ratio='1.2',
            returns_1yr='12.0',
            returns_3yr='30.0',
        )
        Article.objects.create(title='Equity Risk Basics', content='Learn equity risk and volatility.')

    def test_investor_can_invest_and_redirect_to_education(self):
        self.client.force_login(self.investor)
        response = self.client.post(
            reverse('invest_in_fund', args=[self.fund.pk]),
            {'amount': '10000.00', 'nav_price': '100.00'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn('/education/?fund=', response.url)
        self.assertEqual(Investment.objects.filter(user=self.investor, fund=self.fund).count(), 1)

    def test_non_investor_cannot_invest(self):
        self.client.force_login(self.advisor)
        response = self.client.get(reverse('invest_in_fund', args=[self.fund.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Investment.objects.count(), 0)

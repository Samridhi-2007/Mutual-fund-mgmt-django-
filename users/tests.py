from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from advisors.models import Advisor
from education.models import Article
from funds.models import Fund


class RoleBasedCrudFlowTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.admin = user_model.objects.create_user(
            username='admin_user',
            email='admin@example.com',
            password='StrongPass123!',
            role='ADMIN',
        )
        self.advisor_user = user_model.objects.create_user(
            username='advisor_user',
            email='advisor@example.com',
            password='StrongPass123!',
            role='ADVISOR',
        )
        self.investor = user_model.objects.create_user(
            username='investor_user',
            email='investor@example.com',
            password='StrongPass123!',
            role='INVESTOR',
        )

    def test_admin_can_crud_funds(self):
        self.client.force_login(self.admin)

        create_response = self.client.post(
            reverse('fund_create'),
            {
                'name': 'Bluechip Growth',
                'category': 'Equity',
                'risk_level': 'High',
                'expense_ratio': '1.2',
                'returns_1yr': '14.2',
                'returns_3yr': '38.1',
            },
        )
        self.assertEqual(create_response.status_code, 302)
        fund = Fund.objects.get(name='Bluechip Growth')

        update_response = self.client.post(
            reverse('fund_update', args=[fund.pk]),
            {
                'name': 'Bluechip Growth Updated',
                'category': 'Equity',
                'risk_level': 'Moderate',
                'expense_ratio': '1.1',
                'returns_1yr': '13.5',
                'returns_3yr': '36.8',
            },
        )
        self.assertEqual(update_response.status_code, 302)
        fund.refresh_from_db()
        self.assertEqual(fund.name, 'Bluechip Growth Updated')

        delete_response = self.client.post(reverse('fund_delete', args=[fund.pk]))
        self.assertEqual(delete_response.status_code, 302)
        self.assertFalse(Fund.objects.filter(pk=fund.pk).exists())

    def test_investor_cannot_create_fund(self):
        self.client.force_login(self.investor)
        response = self.client.get(reverse('fund_create'))
        self.assertEqual(response.status_code, 403)

    def test_advisor_can_crud_education_articles(self):
        self.client.force_login(self.advisor_user)

        create_response = self.client.post(
            reverse('article_create'),
            {'title': 'How SIP Works', 'content': 'SIP helps with rupee cost averaging.'},
        )
        self.assertEqual(create_response.status_code, 302)
        article = Article.objects.get(title='How SIP Works')

        update_response = self.client.post(
            reverse('article_update', args=[article.pk]),
            {'title': 'How SIP Works Better', 'content': 'Updated content for investor education.'},
        )
        self.assertEqual(update_response.status_code, 302)
        article.refresh_from_db()
        self.assertEqual(article.title, 'How SIP Works Better')

        delete_response = self.client.post(reverse('article_delete', args=[article.pk]))
        self.assertEqual(delete_response.status_code, 302)
        self.assertFalse(Article.objects.filter(pk=article.pk).exists())

    def test_admin_can_crud_advisors(self):
        self.client.force_login(self.admin)

        create_response = self.client.post(
            reverse('advisor_create'),
            {
                'name': 'Rahul Sharma',
                'email': 'rahul.sharma@example.com',
                'expertise': 'Retirement Planning',
                'experience_years': 9,
            },
        )
        self.assertEqual(create_response.status_code, 302)
        advisor = Advisor.objects.get(email='rahul.sharma@example.com')

        update_response = self.client.post(
            reverse('advisor_update', args=[advisor.pk]),
            {
                'name': 'Rahul Sharma',
                'email': 'rahul.sharma@example.com',
                'expertise': 'Tax Saving Funds',
                'experience_years': 10,
            },
        )
        self.assertEqual(update_response.status_code, 302)
        advisor.refresh_from_db()
        self.assertEqual(advisor.expertise, 'Tax Saving Funds')

        delete_response = self.client.post(reverse('advisor_delete', args=[advisor.pk]))
        self.assertEqual(delete_response.status_code, 302)
        self.assertFalse(Advisor.objects.filter(pk=advisor.pk).exists())

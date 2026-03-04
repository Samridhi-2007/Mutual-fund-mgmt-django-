from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import FundForm
from .models import Fund
from users.mixins import RoleRequiredMixin


class FundListView(ListView):
    model = Fund
    template_name = 'funds/fund_list.html'
    context_object_name = 'funds'


class FundDetailView(DetailView):
    model = Fund
    template_name = 'funds/fund_detail.html'
    context_object_name = 'fund'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fund = self.object

        explanation = [
            f'{fund.name} is a {fund.category} fund with a {fund.risk_level} risk profile.',
            f'Expense ratio is {fund.expense_ratio}%, which impacts net returns over time.',
            f'Historical returns are {fund.returns_1yr}% (1Y) and {fund.returns_3yr}% (3Y).',
            'Past performance does not guarantee future returns; align with your goals and risk tolerance.',
        ]
        context['fund_explanation'] = explanation
        return context


class FundCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    allowed_roles = ('ADMIN',)
    model = Fund
    form_class = FundForm
    template_name = 'funds/fund_form.html'
    success_url = reverse_lazy('fund_list')

    def form_valid(self, form):
        messages.success(self.request, 'Fund created successfully.')
        return super().form_valid(form)


class FundUpdateView(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    allowed_roles = ('ADMIN',)
    model = Fund
    form_class = FundForm
    template_name = 'funds/fund_form.html'
    success_url = reverse_lazy('fund_list')

    def form_valid(self, form):
        messages.success(self.request, 'Fund updated successfully.')
        return super().form_valid(form)


class FundDeleteView(LoginRequiredMixin, RoleRequiredMixin, DeleteView):
    allowed_roles = ('ADMIN',)
    model = Fund
    template_name = 'funds/fund_confirm_delete.html'
    success_url = reverse_lazy('fund_list')

    def form_valid(self, form):
        messages.success(self.request, 'Fund deleted successfully.')
        return super().form_valid(form)


def compare_funds(request):
    funds = Fund.objects.all()
    comparison = None

    if request.method == 'POST':
        fund1_id = request.POST.get('fund1')
        fund2_id = request.POST.get('fund2')

        if fund1_id and fund2_id and fund1_id != fund2_id:
            try:
                comparison = {
                    'fund1': Fund.objects.get(pk=fund1_id),
                    'fund2': Fund.objects.get(pk=fund2_id),
                }
            except Fund.DoesNotExist:
                messages.error(request, 'One or both selected funds do not exist.')
        else:
            messages.error(request, 'Please select two different funds.')

    return render(request, 'funds/compare.html', {'funds': funds, 'comparison': comparison})


def risk_analysis(request):
    funds = Fund.objects.all()
    total_funds = funds.count()

    buckets = {'Low': 0, 'Moderate': 0, 'High': 0, 'Other': 0}
    for fund in funds:
        level = (fund.risk_level or '').strip().lower()
        if level in {'low', 'low risk'}:
            buckets['Low'] += 1
        elif level in {'moderate', 'medium', 'moderate risk', 'medium risk'}:
            buckets['Moderate'] += 1
        elif level in {'high', 'high risk', 'very high'}:
            buckets['High'] += 1
        else:
            buckets['Other'] += 1

    context = {
        'total_funds': total_funds,
        'risk_buckets': buckets,
        'funds': funds,
    }
    return render(request, 'funds/risk_analysis.html', context)

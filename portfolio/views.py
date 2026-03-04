from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from funds.models import Fund

from .forms import InvestmentForm
from .models import Investment


@login_required
def my_investments(request):
    investments = Investment.objects.filter(user=request.user).select_related('fund')
    total_invested = sum(item.amount for item in investments) if investments else Decimal('0.00')
    return render(
        request,
        'portfolio/my_investments.html',
        {'investments': investments, 'total_invested': total_invested},
    )


@login_required
def invest_in_fund(request, fund_id):
    if request.user.role != 'INVESTOR':
        messages.error(request, 'Only investors can place investments.')
        return redirect('fund_detail', pk=fund_id)

    fund = get_object_or_404(Fund, pk=fund_id)

    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            nav_price = form.cleaned_data['nav_price']
            units = amount / nav_price

            Investment.objects.create(
                user=request.user,
                fund=fund,
                amount=amount,
                nav_price=nav_price,
                units_purchased=units.quantize(Decimal('0.0001')),
            )

            messages.success(
                request,
                f'Investment successful in {fund.name}. Continue with recommended education content.',
            )
            education_url = f"{reverse('education')}?fund={fund.pk}"
            return redirect(education_url)
    else:
        form = InvestmentForm()

    return render(request, 'portfolio/invest_form.html', {'fund': fund, 'form': form})

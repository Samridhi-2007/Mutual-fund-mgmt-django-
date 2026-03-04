from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from funds.models import Fund
from .forms import ArticleForm
from .models import Article
from users.mixins import RoleRequiredMixin


class ArticleListView(ListView):
    model = Article
    template_name = 'education/education.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fund_id = self.request.GET.get('fund')
        recommended_articles = Article.objects.none()
        selected_fund = None

        if fund_id:
            try:
                selected_fund = Fund.objects.get(pk=fund_id)
                keyword_1 = selected_fund.category.split()[0]
                keyword_2 = selected_fund.risk_level.split()[0]
                recommended_articles = Article.objects.filter(
                    Q(title__icontains=keyword_1)
                    | Q(content__icontains=keyword_1)
                    | Q(title__icontains=keyword_2)
                    | Q(content__icontains=keyword_2)
                )[:5]
            except Fund.DoesNotExist:
                selected_fund = None

        context['selected_fund'] = selected_fund
        context['recommended_articles'] = recommended_articles
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'education/article_detail.html'
    context_object_name = 'article'


class ArticleCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    allowed_roles = ('ADMIN', 'ADVISOR')
    model = Article
    form_class = ArticleForm
    template_name = 'education/article_form.html'
    success_url = reverse_lazy('education')

    def form_valid(self, form):
        messages.success(self.request, 'Article created successfully.')
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    allowed_roles = ('ADMIN', 'ADVISOR')
    model = Article
    form_class = ArticleForm
    template_name = 'education/article_form.html'
    success_url = reverse_lazy('education')

    def form_valid(self, form):
        messages.success(self.request, 'Article updated successfully.')
        return super().form_valid(form)


class ArticleDeleteView(LoginRequiredMixin, RoleRequiredMixin, DeleteView):
    allowed_roles = ('ADMIN', 'ADVISOR')
    model = Article
    template_name = 'education/article_confirm_delete.html'
    success_url = reverse_lazy('education')

    def form_valid(self, form):
        messages.success(self.request, 'Article deleted successfully.')
        return super().form_valid(form)

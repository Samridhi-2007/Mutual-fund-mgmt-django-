from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import AdvisorForm
from .models import Advisor
from users.mixins import RoleRequiredMixin


class AdvisorListView(ListView):
    model = Advisor
    template_name = 'advisors/advisor_list.html'
    context_object_name = 'advisors'


class AdvisorDetailView(DetailView):
    model = Advisor
    template_name = 'advisors/advisor_detail.html'
    context_object_name = 'advisor'


class AdvisorCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    allowed_roles = ('ADMIN',)
    model = Advisor
    form_class = AdvisorForm
    template_name = 'advisors/advisor_form.html'
    success_url = reverse_lazy('advisor_list')

    def form_valid(self, form):
        messages.success(self.request, 'Advisor created successfully.')
        return super().form_valid(form)


class AdvisorUpdateView(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    allowed_roles = ('ADMIN',)
    model = Advisor
    form_class = AdvisorForm
    template_name = 'advisors/advisor_form.html'
    success_url = reverse_lazy('advisor_list')

    def form_valid(self, form):
        messages.success(self.request, 'Advisor updated successfully.')
        return super().form_valid(form)


class AdvisorDeleteView(LoginRequiredMixin, RoleRequiredMixin, DeleteView):
    allowed_roles = ('ADMIN',)
    model = Advisor
    template_name = 'advisors/advisor_confirm_delete.html'
    success_url = reverse_lazy('advisor_list')

    def form_valid(self, form):
        messages.success(self.request, 'Advisor deleted successfully.')
        return super().form_valid(form)

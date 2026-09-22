from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from .forms import ContractForm
from .models import Contract


class ContractListView(PermissionRequiredMixin, ListView):
    """Страница списка контрактов."""
    permission_required = 'contracts.view_contract'
    model = Contract


class ContractDetailView(PermissionRequiredMixin, DetailView):
    """Детальная страница контракта: неизменяемая форма и кнопки действий."""
    permission_required = 'contracts.view_contract'
    model = Contract


    def get_context_data(self, **kwargs):
        """Готовит форму с данными контракта и выключенными полям"""
        context = super().get_context_data(**kwargs)
        form = ContractForm(instance=self.object)
        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
        context['form'] = form
        return context


class ContractCreateView(PermissionRequiredMixin, CreateView):
    """Страница создания контракта."""
    permission_required = 'contracts.add_contract'
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contract_create.html'


class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    """Страница редактирования контракта."""
    permission_required = 'contracts.change_contract'
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contract_update.html'


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    """Страница подтверждения удаления контракта."""
    permission_required = 'contracts.delete_contract'
    model = Contract
    success_url = reverse_lazy('contracts_list')

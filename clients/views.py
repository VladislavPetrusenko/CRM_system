from typing import Any
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import ActiveClientCreateForm, ActiveClientForm
from .models import ActiveClient
from leads.models import Lead


class ActiveClientListView(PermissionRequiredMixin, ListView):
    """Страница списка активных клиентов."""
    permission_required = 'clients.view_activeclient'
    model = ActiveClient
    template_name = 'clients/client_list.html'
    context_object_name = 'client_list'


class ActiveClientDetailView(PermissionRequiredMixin, DetailView):
    """Детальная страница активного клиента: неизменяемая форма."""
    permission_required = 'clients.view_activeclient'
    model = ActiveClient
    template_name = 'clients/client_detail.html'


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """Готовит форму с данными клиента и выключенными полями."""
        context = super().get_context_data(**kwargs)
        form = ActiveClientForm(instance=self.object)
        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
        context['form'] = form
        return context


class ActiveClientCreateView(PermissionRequiredMixin, CreateView):
    """Перевод потенциального клиента в активного с созданием контракта."""
    permission_required = 'clients.add_activeclient'
    form_class = ActiveClientCreateForm
    template_name = 'clients/client_create.html'


    def get_initial(self) -> dict[str, Any]:
        """Предзаполняет поле лида из query-параметра ?lead=."""
        initial = super().get_initial()
        lead_id = self.request.GET.get('lead')
        if lead_id:
            try:
                initial['lead'] = Lead.objects.get(pk=lead_id)
            except (Lead.DoesNotExist, ValueError):
                pass
        return initial


    def form_valid(self, form):
        """Создаёт контракт и активного клиента, перенаправляет на его страницу."""
        contract = form.save()
        active_client = ActiveClient.objects.create(lead=form.cleaned_data['lead'], contract=contract)
        return redirect(active_client)


class ActiveClientUpdateView(PermissionRequiredMixin, UpdateView):
    """Страница редактирования активного клиента."""
    permission_required = 'clients.change_activeclient'
    model = ActiveClient
    form_class = ActiveClientForm
    template_name = 'clients/client_update.html'


class ActiveClientDeleteView(PermissionRequiredMixin, DeleteView):
    """Страница подтверждения удаления активного клиента."""
    permission_required = 'clients.delete_activeclient'
    model = ActiveClient
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('clients_list')

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import LeadForm
from .models import Lead


class LeadListView(PermissionRequiredMixin, ListView):
    """Страница списка потенциальных клиентов."""
    permission_required = 'leads.view_lead'
    model = Lead


class LeadDetailView(PermissionRequiredMixin, DetailView):
    """Детальная страница лида: неизменяемая форма и кнопки действий."""
    permission_required = 'leads.view_lead'
    model = Lead


    def get_context_data(self, **kwargs):
        """Готовит форму с данными лида и выключенными полями."""
        context = super().get_context_data(**kwargs)
        form = LeadForm(instance=self.object)
        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
        context['form'] = form
        return context


class LeadCreateView(PermissionRequiredMixin, CreateView):
    """Страница создания потенциального клиента."""
    permission_required = 'leads.add_lead'
    model = Lead
    form_class = LeadForm
    template_name = 'leads/lead_create.html'


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    """Страница редактирования потенциального клиента."""
    permission_required = 'leads.change_lead'
    model = Lead
    form_class = LeadForm
    template_name = 'leads/lead_update.html'


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    """Страница подтверждения удаления потенциального клиента."""
    permission_required = 'leads.delete_lead'
    model = Lead
    success_url = reverse_lazy('leads_list')
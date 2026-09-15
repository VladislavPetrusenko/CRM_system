from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import CompaignForm
from .models import Compaign


class CompaignListView(PermissionRequiredMixin, ListView):
    """Страница списка рекламных кампаний."""
    permission_required = 'compaigns.view_compaign'
    model = Compaign


class CompaignDetailView(PermissionRequiredMixin, DetailView):
    """Детальная страница кампании: неизменяемая форма и кнопки действий."""
    permission_required = 'compaigns.view_compaign'
    model = Compaign


    def get_context_data(self, **kwargs):
        """Готовит форму с данными кампании и выключенными полями."""
        context = super().get_context_data(**kwargs)
        form = CompaignForm(instance=self.object)
        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
        context['form'] = form
        return context


class CompaignCreateView(PermissionRequiredMixin, CreateView):
    """Страница создания рекламной кампании."""
    permission_required = 'compaigns.add_compaign'
    model = Compaign
    form_class = CompaignForm
    template_name = 'compaigns/compaign_create.html'


class CompaignUpdateView(PermissionRequiredMixin, UpdateView):
    """Страница редактирования рекламной кампании."""
    permission_required = 'compaigns.change_compaign'
    model = Compaign
    form_class = CompaignForm
    template_name = 'compaigns/compaign_update.html'


class CompaignDeleteView(PermissionRequiredMixin, DeleteView):
    """Страница подтверждения удаления рекламной кампании."""
    permission_required = 'compaigns.delete_compaign'
    model = Compaign
    success_url = reverse_lazy('compaigns_list')
    
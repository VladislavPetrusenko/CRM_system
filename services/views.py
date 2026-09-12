from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from services.forms import ServiceForm
from services.models import Service


class ServiceListView(PermissionRequiredMixin, ListView):
    """Страница списка услуг."""
    permission_required = 'services.view_service'
    model = Service


class ServiceDetailView(PermissionRequiredMixin, DetailView):
    """Детальная страница услуги: неизменяемая форма и кнопки действий."""
    permission_required = 'services.view_service'
    model = Service


    def get_context_data(self, **kwargs):
        """Готовит форму с данными услуги и выключенными полями."""
        context = super().get_context_data(**kwargs)
        form = ServiceForm(instance=self.object)
        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
        context['form'] = form
        return context


class ServiceCreateView(PermissionRequiredMixin, CreateView):
    """Страница создания услуги."""
    permission_required = 'services.add_service'
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_create.html'


class ServiceUpdateView(PermissionRequiredMixin, UpdateView):
    """Страница редактирования услуги."""
    permission_required = 'services.change_service'
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_update.html'


class ServiceDeleteView(PermissionRequiredMixin, DeleteView):
    """Страница подтверждения удаления услуги."""
    permission_required = 'services.delete_service'
    model = Service
    success_url = reverse_lazy('services_list')

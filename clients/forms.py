from django import forms
from .models import ActiveClient
from contracts.forms import ContractForm
from leads.models import Lead


class ActiveClientForm(forms.ModelForm):
    """Форма редактирования активного клиента."""


    class Meta:
        model = ActiveClient
        fields = ['lead', 'contract']
        widgets = {
            'lead': forms.Select(attrs={'class': 'form-control'}),
            'contract': forms.Select(attrs={'class': 'form-control'})
        }


class ActiveClientCreateForm(ContractForm):
    """Форма перевода лида в активного клиента: лида + данные нового контракта."""
    lead = forms.ModelChoiceField(
        queryset=Lead.objects.filter(active_client__isnull=True),
        label='Потенциальный клиент',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    field_order = ['lead', 'name', 'service', 'file', 'conclusion_date', 'end_date', 'amount']

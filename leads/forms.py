from django import forms
from leads.models import Lead


class LeadForm(forms.ModelForm):
    """Форма создания и редактирования потенциального клиента."""


    class Meta:
        model = Lead
        fields = ['full_name', 'phone', 'email', 'compaign']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'compaign': forms.Select(attrs={'class': 'form-control'})
        }
        
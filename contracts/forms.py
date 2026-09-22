from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
    """Форма создания и редактирования контракта."""


    class Meta:
        model = Contract
        fields = ['name', 'service', 'file', 'conclusion_date', 'end_date', 'amount']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'conclusion_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d'
            ),
            'end_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d'
            ),
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
        }
        
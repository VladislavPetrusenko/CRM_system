from django import forms
from compaigns.models import Compaign


class CompaignForm(forms.ModelForm):
    """Форма создания и редактирования рекламной кампании."""


    class Meta:
        model = Compaign
        fields = ['name', 'service', 'channel', 'budget']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'channel': forms.Select(attrs={'class': 'form-control'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control'})
        }
        
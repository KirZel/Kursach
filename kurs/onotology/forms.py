from django import forms

from .models import TableForFormCheck


class GetJanr(forms.ModelForm):

    class Meta:
        model = TableForFormCheck
        fields = '__all__'
        labels = {
            'Instr_name': 'Инструмент',
            'Harak_name': 'Характеристика',
            'Harak_value': 'Значение',
        }

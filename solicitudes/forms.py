from django import forms
from .models import Solicitud

class solicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'user',
            'closeDate',
            'status'
        ]

        labels = {
            'user': 'user',
            'closeDate' : 'CloseDate',
            'status' : 'Status'
        }
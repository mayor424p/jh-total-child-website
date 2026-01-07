from django import forms
from .models import AdmissionApplication

class AdmissionForm(forms.ModelForm):
   

    class Meta:
        model = AdmissionApplication
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

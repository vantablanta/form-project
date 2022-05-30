from .models import SubscriptionModel
from django.forms import ModelForm
from django import forms 

class SubscriptionForm(ModelForm):
    class Meta():
        model = SubscriptionModel
        fields  = ['email', 'name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

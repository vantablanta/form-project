from .models import SubscriptionModel
from django.forms import ModelForm

class SubscriptionForm(ModelForm):
    class Meta():
        model = SubscriptionModel
        fields  = '__all__'
        widgets = {}

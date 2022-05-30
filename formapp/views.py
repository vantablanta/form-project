from django.http import HttpResponse
from django.shortcuts import render
from .forms import SubscriptionForm
from .models import SubscriptionModel
from .emails import send_welcome_email
# Create your views here.
def home(request):
    form = SubscriptionForm()
    
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            send_welcome_email(name,email)
            context={'name':name, 'email':email}
            return render(request, 'formapp/succes.html', context)
       
    context = {'form': form}
    return render(request, 'formapp/subscription.html', context)
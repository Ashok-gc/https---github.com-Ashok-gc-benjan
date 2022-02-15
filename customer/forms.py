from socket import fromshare
from django import forms
from customer.models import Customer, catering

class CustomerForm(forms.ModelForm):
    class Meta:
     model = Customer
     fields = ("__all__")

class CateringForm(forms.ModelForm):
    class Meta:
     model = catering
     fields = ("__all__")
     
     
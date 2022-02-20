
from django import forms
from customer.models import Customer, catering, contact_us

class CustomerForm(forms.ModelForm):
    class Meta:
     model = Customer
     fields = ("__all__")

class CateringForm(forms.ModelForm):
    class Meta:
     model = catering
     fields = ("__all__")

class ContactForm(forms.ModelForm):
    class Meta:
     model = contact_us
     fields = ("__all__")

class Updatecustomer(forms.ModelForm):
    class Meta:
     model = Customer
     fields = ("username", "email", "number", "password")    
     
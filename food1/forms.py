from socket import fromshare
from django import forms
from food1.models import Food1

class FoodForm(forms.ModelForm):
    class Meta:
     model = Food1
     fields = ("__all__")


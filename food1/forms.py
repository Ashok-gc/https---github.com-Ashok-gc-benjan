from socket import fromshare
from django import forms
from food1.models import Food1, blog

class FoodForm(forms.ModelForm):
    class Meta:
     model = Food1
     fields = ("__all__")

class UpdateForm(forms.ModelForm):
    class Meta:
     model = Food1
     fields = ("Name", "Price", "Type", "description")


class BlogForm(forms.ModelForm):
    class Meta:
     model = blog
     fields = ("blog_Name", "blog_Photo", "blog_description")


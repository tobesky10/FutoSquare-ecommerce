from django.forms import ModelForm
from django import forms
from ecomstore.models import Product


class Productform(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['user']


class Profileform(forms.Form):
    first_name = forms.CharField(label='Firstname', max_length=15, required=True)
    last_name = forms.CharField(label='Lastname', max_length=15, required=True)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', max_length=256, required=True, widget=forms.PasswordInput)


class Loginform(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', max_length=256, required=True, widget=forms.PasswordInput)


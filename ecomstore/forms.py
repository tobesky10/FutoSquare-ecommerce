from django.forms import ModelForm
from django import forms
from ecomstore.models import Product


class Productform(forms.Form):
    name = forms.CharField(label='Name', max_length=15, required=True,
                                 widget=forms.TextInput(attrs={'class': 'input', }))
    price = forms.CharField(label='Price', max_length=16, required=False,
                            widget=forms.NumberInput(attrs={'class': 'input', }))
    description = forms.CharField(label='Description', max_length=60, required=True,
                                  widget=forms.Textarea(attrs={'class': 'input', }))

    product_image1 = forms.ImageField(label='Product Image 1')
    product_image2 = forms.ImageField(label='Product Image 2')
    product_image3 = forms.ImageField(label='Product Image 3')


class Profileform(forms.Form):
    first_name = forms.CharField(label='Firstname', max_length=15, required=True,
                                 widget=forms.TextInput(attrs={'class': 'input', }))
    last_name = forms.CharField(label='Lastname', max_length=15, required=True,
                                widget=forms.TextInput(attrs={'class': 'input', }))
    email = forms.EmailField(label='Email', required=True,
                             widget=forms.EmailInput(attrs={'class': 'input', }))
    password_1 = forms.CharField(label='Password', max_length=256, required=True,
                                 widget=forms.PasswordInput(attrs={'class': 'input'}))
    password_2 = forms.CharField(label=' Confirm Password', max_length=256, required=True,
                                 widget=forms.PasswordInput(attrs={'class': 'input'}))


class UpdateProfileform(forms.Form):
    avatar = forms.ImageField(label='Profile Photo')
    first_name = forms.CharField(label='Firstname', max_length=15, required=True,
                                 widget=forms.TextInput(attrs={'class': 'input', }))
    last_name = forms.CharField(label='Lastname', max_length=15, required=True,
                                widget=forms.TextInput(attrs={'class': 'input', }))
    email = forms.EmailField(label='Email', required=True,
                             widget=forms.EmailInput(attrs={'class': 'input', }))
    password_1 = forms.CharField(label='Password', max_length=256, required=True,
                                 widget=forms.PasswordInput(attrs={'class': 'input'}))
    phone = forms.CharField(label='phone', max_length=16, required=False,
                            widget=forms.NumberInput(attrs={'class': 'input',}))


class Loginform(forms.Form):
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'email', }))
    password = forms.CharField(label='Password', max_length=256, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'password'}))


from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Currency, Customer, Wallet

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        
class RegisterCurrency(forms.ModelForm):
    class Meta:
        model=Currency
        fields="__all__"
        
class RegisterWallet(forms.ModelForm):
    class Meta:
        model=Wallet
        fields="__all__"
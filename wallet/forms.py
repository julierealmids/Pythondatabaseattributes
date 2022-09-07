from dataclasses import fields
from pyexpat import model
from sqlite3 import paramstyle
from django import forms
from .models import Account, Card, Currency, Customer, Loan_model, Notification, Receipt, Reward, Third_Party, Transaction, Wallet

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
        
class RegisterAccount(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__"
        
class RegisterThird_party(forms.ModelForm):
    class Meta:
        model=Third_Party
        fields="__all__"
class RegisterTransaction(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__"
class RegisterCard(forms.ModelsForm):
    class Meta:
        model=Card
        feilds="__all__"
class RegisterReceipt(forms.ModelForms):
    class Meta:
        model=Receipt
        fields="__all__"
class RegisterNotification(forms.ModelForms):
    class Meta:
        model=Notification
        fields="__all__"
class RegisterLoan_model(forms.ModelForms):
    class Meta:
        model=Loan_model
        fields="__all__"
class RegisterReward(forms.ModelForm):
    class Meta:
        model=Reward
        fields="__all__"
from dataclasses import field, fields
from locale import currency
from pyexpat import model
from wallet.models import Customer,Wallet,Currency,Account,Third_Party,Transaction,Card,Receipt,Notification,Loan_model,Reward
from rest_framework import serializers

class Customerserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Customer
        fields=('first_name','last_name',' gender=models',' address',' age=models','nationality',' id_number','phone_number','  email','profile_picture',' marital_status','signature','mployment_status')
        
class Walletserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Wallet
        fields=('balance','customer','pin','currency','active','datecreated')
        
class Currencyserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Currency
        fields=('Symbol','name','country')
        
class Accountserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Account
        fields=('account_type','acount_name','wallet')
        
class Third_Party(serializers.HyperlinkModelSerializer):
    class Meta:
        model=Third_Party
        fields=('full_name','email','phone_number','transaction','currency','account','status')
            
class Transaction(serializers.HyperlinkModelSerializer):
    class Meta:
        model=Transaction
        fields=('transaction','account_origin','third_party','datetime','status')
        
class Card(serializers.HyperlinkModelSerializer):
    class Meta:
        model=Card
        fields=('date_issued','card_status','security_code','signature','issuer','account')
        
class Receipt(serializers.HyperlinkModelSerializer):
    class Meta:
        model=Receipt
        fields=('date','transaction','receipt_file')
        
class Notification(serializers.HyperlinkModelSerializer):
    class Meta:
        model=Notification
        fields=('datecreated','message','status','image')

class Loan_model(serializers.HyperlinkModelSerializer):
    class Meta:
        model=Loan_model
        fields=('amount','wallet','datetime','loan','payment','loan_terms','payment_due_date','guaranter','balance','duration','interest','status')
        
class Reward(serializers.HyperlinkModelSerializer):
    class Meta:
        model=Reward
        fields=('wallet','points','date','transaction')       
       
        
from django.shortcuts import redirect, render
from . import models

from wallet.models import Account, Currency, Customer, Wallet
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, Loan_modelRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, Third_partyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

def register_customer(request):
    if request.method == "POST":
          form = CustomerRegistrationForm(request.POST)
          if form.is_valid():
              form.save()
    else:
        form = CustomerRegistrationForm()
        return render(request, 'walletT/register_customer.html',
                  {"form":form})
def list_customer(request):
    customers = models.Customer.objects.all()
    return render (request, 'walletT/customer_list.html',
                   {"customers":customers})
def customer_profile(request,id):
    customers=models.Customer.objects.get(id=id)
    return render (request, 'walletT/customer_profile.html',
                   {"customers":customers})
    
def edit_customer(request,id):
    customers=Customer.objects.get(id=id)
    if request.method=="POST":
        form = CustomerRegistrationForm(request.POST,instance=customers)
        if form.is_valid():
            form.save()
            return redirect("customer_profile",id=customers.id)
        else:
            form=CustomerRegistrationForm(instance=customers)
            return render(request,"wallet/edit_customer.html",{"form":form})
    
def register_currency(request):
    if request.method=="POST":
        form.CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CurrencyRegistrationForm()
    return render(request,'wallet/register_currency.html',
                  {"form":form})   
    
def list_currency(request):
    currency=Currency.objects.all()
    return render(request,"wallet/currency_list.html",{"currency":currency})

def register_wallet(request):
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'wallet/register_wallet.html',
                  {"form":form})  
def list_wallet(request):
    wallet=Wallet.objects.all()
    return render(request,"wallet/wallet_list.html",{"wallet":wallet})

def register_account(request):
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'wallet/register_account.html',
                  {"form":form}) 
    
def list_account(request):
        account=Account.objects.all()
        return render(request,"wallet/account_list.html",{"account":account})
 
    
def register_third_party(request):
    form=Third_partyRegistrationForm()
    return render(request,'wallet/register_third_party.html',
                  {"form":form})  
    
def register_transaction(request):
    form=TransactionRegistrationForm()
    return render(request,'wallet/register_transaction.html',
                  {"form":form})  
    
def register_card(request):
    form=CardRegistrationForm()
    return render(request,'wallet/register_card.html',
                  {"form":form})  
    
def register_receipt(request):
    form=ReceiptRegistrationForm()
    return render(request,'wallet/register_receipt.html',
                  {"form":form})  
    
def register_notification(request):
    form=NotificationRegistrationForm()
    return render(request,'wallet/register_notification.html',
                  {"form":form})
    
def register_loan_model(request):
    form=Loan_modelRegistrationForm()
    return render(request,'wallet/register_loan_model.html',
                  {"form":form}) 
    
def register_reward(request):
    form=RewardRegistrationForm()
    return render(request,'wallet/register_reward.html',
                  {"form":form})     
    


    


















from atexit import register
from unicodedata import name
from django.urls import path


# from wallet.models import wallet
from .views import Customer_profile, list_customers, register_customer,register_wallet,register_currency,register_account,register_third_party,register_transaction,register_card,register_receipt,register_notification,register_loan_model,register_reward
from django .urls import path

urlpatterns = [
    path("register/",register_customer,name="registration"),
    path("currency/",register_currency,name="registration"),
    path("wallet/",register_wallet,name="registration"),
    path("account/",register_account,name="registration"),
    path("third_party/",register_third_party,name="registration"),
    path("transaction/",register_transaction,name="registration"),
    path("card/",register_card,name="registration"),
    path("receipt/",register_receipt,name="registartion"),
    path("notification/",register_notification,name="registration"),
    path("loan_model/",register_loan_model,name="registration"),
    path("reward/",register_reward,name="registration"),
    path("list1",list_customers,name="list_customers"),
    path("customers/<int:1>",Customer_profile,name="Customer_profile"),
    path("customers/edit/int:id>/,edit_customer,name="edit_customer"),
    
    # path("wallet/",include("wallet.urls")),
]



from atexit import register
from unicodedata import name
from django.urls import path


# from wallet.models import wallet
from .views import register_customer,register_wallet,register_currency,register_account,register_third_party,register_transaction,register_card,register_receipt,register_notification,register_loan_model,register_reward
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
    
    # path("wallet/",include("wallet.urls")),
]



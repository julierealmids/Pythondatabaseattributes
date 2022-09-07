from atexit import register
from unicodedata import name
from django.urls import path

from wallet.forms import RegisterWallet

# from wallet.models import wallet
from .views import register_customer,register_wallet,register_currency,register_account,register_third_party,register_transaction,register_card,register_receipt,register_notification,register_loan_model,register_reward
from django .urls import path

urlpatterns = [
    path("register/",register_customer,name="registration"),
    path("register/",register_currency,name="registration"),
    path("register/",register_wallet,name="registration"),
    path("register/",register_account,name="registration"),
    path("register/",register_third_party,name="registration"),
    path("register/",register_transaction,name="registration"),
    path("register/",register_card,name="registration"),
    path("register/",register_receipt,name="registartion"),
    path("register/",register_notification,name="registration"),
    path("register/",register_loan_model,name="registration"),
    path("register/",register_reward,name="registration"),
    
    # path("wallet/",include("wallet.urls")),
]



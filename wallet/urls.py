from unicodedata import name
from django.urls import path

# from wallet.models import wallet
from .views import register_customer
from django .urls import path

urlpatterns = [
    path("register/",register_customer,name="registration"),
    # path("wallet/",include("wallet.urls")),
]



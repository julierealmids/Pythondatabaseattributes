from django.urls import include, path
from rest_framework import routers
from wallet import views

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'wallet', views.WalletViewSet)
router.register(r'currency', views.CurrencyViewSet)
router.register(r'account', views.AccountItemViewSet)
router.register(r'third_party', views.Thrid_partyItemViewSet)
router.register(r'transaction', views.TranscationItemViewSet)
router.register(r'card', views.CardItemViewSet)
router.register(r'receipt', views.ReceiptItemViewSet)
router.register(r'notification', views.NotificationItemViewSet)
router.register(r'loan_model', views.Loan_modelItemViewSet)
router.register(r'reward', views.RewardItemViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


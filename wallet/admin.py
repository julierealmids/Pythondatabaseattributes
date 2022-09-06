# from django.contrib import admin

# # Register your models here.
# from .models import Customer

# class CustomerAdmin(admin.ModelAdmin):
#     list_display=("first_name","last_name",)
from django.contrib import admin
from .models import Account, Card, Currency, Customer, Loan_model, Notification, Receipt, Reward, Third_Party, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email",)
    search_fields=("first_name","last_name",)
    
class Loan_modelAdmin(admin.ModelAdmin):
    list_display=("loan_type","duration","payment_due_date",)
    search_fields=("loan_type","duration",)
    
class RewardAdmin(admin.ModelAdmin):
    list_display=("wallet","transaction","points")
    search_fields=("transaction","points")
    
class CardAdmin(admin.ModelAdmin):
    list_display=("account","date_issued","card_status")
    search_fields=("account","card_status")
    

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(Third_Party)
admin.site.register(Transaction)
admin.site.register(Card,CardAdmin)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan_model,Loan_modelAdmin)
admin.site.register(Reward,RewardAdmin)
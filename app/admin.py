from django.contrib import admin
from .models import CustomUser, Account, KYC, TransferDetails, Payment, Transaction, Loan, Card, Transfer, Support, Notification
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Loan)
admin.site.register(Card)
admin.site.register(Transfer)
admin.site.register(TransferDetails)
admin.site.register(Notification)
admin.site.register(Support)
admin.site.register(Payment)
admin.site.register(KYC)
 




from django.contrib import admin
from expenditure_register.models import *


class ExpenditureRegisterAdmin(admin.ModelAdmin):
    list_display = ['budget_type', 'year', 'organization', 'special_organization']

class AccountAdmin(admin.ModelAdmin):
    list_display = ['number', 'category', 'subcategory', 'description', 'expenditure_register']

class TransferAdmin(admin.ModelAdmin):
    list_display = ['expenditure_register', 'outgoing_account', 'incoming_account', 'amount', 'protocol', 'date', 'diavgeia_string', 'diavgeia_date']

class CreditAdmin(admin.ModelAdmin):
    list_display = ['credit_reform', 'credit', 'disposed_percentage', 'date_of_disposal', 'account', 'transfer']
    
class DebitCreditAdmin(admin.ModelAdmin):
    list_display = ['debit', 'debit_protocol_number', 'debit_date', 'diavgeia_string', 'diavgeia_date', 'account']

class RecallTransferAdmin(admin.ModelAdmin):
    list_display = ['recall', 'recall_protocol_number', 'recall_date', 'diavgeia_string', 'diavgeia_date', 'account']

class ContractAdmin(admin.ModelAdmin):
    list_display = ['debit', 'protocol_number', 'date', 'diavgeia_string', 'diavgeia_date']

class RequestForPaymentOrInvoiceAdmin(admin.ModelAdmin):
    list_display = ['owned_to', 'debit', 'afm', 'creditor_is_abroad', 'transaction_is_commercial', 'invoice_series', 'invoice_number', 'invoice_date', 'payment_due_date', 'obligation_creation_date']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'payment_type_choice', 'number', 'document_type', 'date', 'payment_amount', 'payment_amount_to_third_persons', 'setoff_payment_amount'] 


# Register your models here.
admin.site.register(ExpenditureRegister, ExpenditureRegisterAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Credit, CreditAdmin)
admin.site.register(Transfer, TransferAdmin)
admin.site.register(Debit, DebitCreditAdmin)
admin.site.register(Recall, RecallTransferAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(RequestForPaymentOrInvoice, RequestForPaymentOrInvoiceAdmin)
admin.site.register(Payment, PaymentAdmin)


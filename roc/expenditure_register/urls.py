from django.urls import path
from .views import *

urlpatterns = [
    path('', ExpenditureRegisterListView.as_view(), name='home'),
    path('register/list', ExpenditureRegisterListView.as_view(), name = 'register_list'),
    path('register/<int:pk>/details', ExpenditureRegisterDetailView.as_view(), name = 'register_details'),
    path('register/<int:pk>/update', ExpenditureRegisterUpdateView.as_view(), name = 'register_update'),
    path('register/create', ExpenditureRegisterCreateView.as_view(), name = 'register_create'),
    path('register/<int:pk>/delete', ExpenditureRegisterDeleteView.as_view(), name = 'register_delete'),
    path('register/<int:register_pk>/report', RegisterReportView.as_view(), name = 'register_report'),
    path('register/<int:register_pk>/<int:reference_day>/<int:reference_month>/<int:reference_year>/report_to_xlsx', RegisterReportToXlsxView.as_view(), name = 'register_report_to_xlsx'),
    path('register/recall_request_in_pdf', GenerateRecallRequestFormView.as_view(), name = 'recall_request_in_pdf'),
    # path('register/recall_request_print_pdf', GenerateRecallRequestInPdfView.as_view(), name = 'recall_request_print_pdf'),
    path('account/<int:register_pk>/list', AccountListView.as_view(), name = 'account_list'),
    path('account/<int:register_pk>/create', AccountCreateView.as_view(), name = 'account_create'),
    path('account/<int:register_pk>/<int:pk>/update', AccountUpdateView.as_view(), name = 'account_update'),
    path('account/<int:register_pk>/<int:pk>/delete', AccountDeleteView.as_view(), name = 'account_delete'),
    path('credit/<int:register_pk>/<int:account_pk>/create', CreditCreateView.as_view(), name = 'credit_create'),
    path('credit/<int:register_pk>/<int:account_pk>/list', CreditListView.as_view(), name = 'credit_list'),
    # path('credit/<int:pk>/details', CreditDeleteView.as_view(), name = 'credit_details'),
    path('credit/<int:register_pk>/<int:account_pk>/<int:pk>/update', CreditUpdateView.as_view(), name = 'credit_update'),
    path('credit/<int:register_pk>/<int:account_pk>/<int:pk>/delete', CreditDeleteView.as_view(), name = 'credit_delete'),
    path('debit/<int:register_pk>/<int:account_pk>/list', DebitListView.as_view(), name = 'debit_list'),
    path('debit/<int:register_pk>/<int:account_pk>/create', DebitCreateView.as_view(), name = 'debit_create'),
    path('debit/<int:register_pk>/<int:account_pk>/<int:pk>/update', DebitUpdateView.as_view(), name = 'debit_update'),
    path('debit/<int:register_pk>/<int:account_pk>/<int:pk>/delete', DebitDeleteView.as_view(), name = 'debit_delete'),
    path('recall/<int:register_pk>/<int:account_pk>/list', RecallListView.as_view(), name = 'recall_list'),
    path('recall/<int:register_pk>/<int:account_pk>/create', RecallCreateView.as_view(), name = 'recall_create'),
    path('recall/<int:register_pk>/<int:account_pk>/<int:pk>/update', RecallUpdateView.as_view(), name = 'recall_update'),
    path('recall/<int:register_pk>/<int:account_pk>/<int:pk>/delete', RecallDeleteView.as_view(), name = 'recall_delete'),
    path('invoice/<int:register_pk>/<int:account_pk>/<int:debit_pk>/create', RequestForPaymentOrInvoiceCreateView.as_view(), name = 'invoice_create'),
    path('invoice/<int:register_pk>/<int:account_pk>/<int:debit_pk>/list', RequestForPaymentOrInvoiceListView.as_view(), name = 'invoice_list'),
    path('invoice/<int:register_pk>/<int:account_pk>/<int:debit_pk>/<int:pk>/detail', RequestForPaymentOrInvoiceDetailView.as_view(), name = 'invoice_detail'),
    path('invoice/<int:register_pk>/<int:account_pk>/<int:debit_pk>/<int:pk>/update', RequestForPaymentOrInvoiceUpdateView.as_view(), name = 'invoice_update'),
    path('invoice/<int:register_pk>/<int:account_pk>/<int:debit_pk>/<int:pk>/delete', RequestForPaymentOrInvoiceDeleteView.as_view(), name = 'invoice_delete'),
    path('payment/<int:register_pk>/<int:account_pk>/<int:debit_pk>/<int:invoice_pk>/create', PaymentCreateView.as_view(), name = 'payment_create'),
    path('payment/<int:register_pk>/<int:account_pk>/<int:debit_pk>/<int:invoice_pk>/list', PaymentListView.as_view(), name = 'payment_list'),
    path('payment/<int:register_pk>/<int:account_pk>/<int:debit_pk>/<int:invoice_pk>/<int:pk>/detail', PaymentDetailView.as_view(), name = 'payment_detail'),
    path('payment/<int:register_pk>/<int:account_pk>/<int:debit_pk>/<int:invoice_pk>/<int:pk>/update', PaymentUpdateView.as_view(), name = 'payment_update'),
    path('payment/<int:register_pk>/<int:account_pk>/<int:debit_pk>/<int:invoice_pk>/<int:pk>/delete', PaymentDeleteView.as_view(), name = 'payment_delete'),
    path('transfer/<int:register_pk>/create', TransferCreateView.as_view(), name = 'transfer_create'),
    path('transfer/<int:register_pk>/list', TransferListView.as_view(), name = 'transfer_list'),
    path('transfer/<int:register_pk>/<int:pk>/delete', TransferDeleteView.as_view(), name = 'transfer_delete'),
    path('transfer/<int:register_pk>/<int:pk>/update', TransferUpdateView.as_view(), name = 'transfer_update'),
]
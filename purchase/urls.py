from django.urls import path
from . import views
app_name = 'purchase'

urlpatterns = [
    path('purchase_enquiry_request', views.purchase_enquiry_request, name='purchase_enquiry_request'),
    path('purchase_compare_quote', views.purchase_compare_quote, name='purchase_compare_quote'),
    path('confirm_purchase_order', views.confirm_purchase_order, name='confirm_purchase_order'),
    path('purchase_order_invoice_pdf', views.purchase_order_invoice_pdf, name='purchase_order_invoice_pdf'),
    path('purchase_order_tracking', views.purchase_order_tracking, name='purchase_order_tracking'),
    # path('purchase_order_payment_transfer', views.purchase_order_payment_transfer, name='purchase_order_payment_transfer'),
]

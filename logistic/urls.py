from django.urls import path
from . import views
app_name = 'logistic'

urlpatterns = [
    path('logistic_compare_quote', views.logistic_compare_quote, name='logistic_compare_quote'),
    path('logistic_compare_quote', views.logistic_compare_quote, name='logistic_compare_quote'),
    path('confirm_logistic_order', views.confirm_logistic_order, name='confirm_logistic_order'),
    path('logistic_order_invoice_pdf', views.logistic_order_invoice_pdf, name='logistic_order_invoice_pdf'),
    path('logistic_order_tracking', views.logistic_order_tracking, name='logistic_order_tracking'),
    # path('logistic_order_payment_transfer', views.logistic_order_payment_transfer, name='logistic_order_payment_transfer'),
]

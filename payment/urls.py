from django.urls import path
from . import views
app_name = 'payment'

urlpatterns = [
    path('sales_order_payment_collection', views.sales_order_payment_collection, name='sales_order_payment_collection'),
    path('collection_reminder', views.collection_reminder, name='collection_reminder'),
    path('purchase_order_payment_transfer', views.purchase_order_payment_transfer, name='purchase_order_payment_transfer'),
    path('logistic_order_payment_transfer', views.logistic_order_payment_transfer, name='logistic_order_payment_transfer'),
    path('payment_transfer_notification', views.payment_transfer_notification, name='payment_transfer_notification'),
]

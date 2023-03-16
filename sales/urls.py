from django.urls import path
from . import views
app_name = 'sales'

urlpatterns = [
    path('confirm_sales_order', views.confirm_sales_order, name='confirm_sales_order'),
    path('sales_order_invoice_pdf', views.sales_order_invoice_pdf, name='sales_order_invoice_pdf'),
    path('sales_order_tracking', views.sales_order_tracking, name='sales_order_tracking'),
]

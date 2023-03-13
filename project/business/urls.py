from django.urls import path
from . import views
app_name = 'business'

urlpatterns = [
    path('sales_order_expenses', views.sales_order_expenses, name='sales_order_expenses'),
    path('purchase_order_expenses', views.purchase_order_expenses, name='purchase_order_expenses'),
    path('logistic_order_expenses', views.logistic_order_expenses, name='logistic_order_expenses'),
    path('recurring_expenses', views.recurring_expenses, name='recurring_expenses'),
    path('fixed_expenses', views.fixed_expenses, name='fixed_expenses'),

    path('optimization', views.optimization, name='optimization'),
    path('product_performance', views.product_performance, name='product_performance'),
    path('category_performance', views.category_performance, name='category_performance'),
]

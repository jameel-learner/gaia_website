from django.urls import path
from . import views
app_name = 'inventory'

urlpatterns = [
    path('product_stock_check', views.product_stock_check, name='product_stock_check'),
    path('product_stock_update', views.product_stock_update, name='product_stock_update'),
    path('product_costing', views.product_costing, name='product_costing'),
    path('product_pricing', views.product_pricing, name='product_pricing'),
]

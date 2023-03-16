from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('forgot', views.forgot, name='forgot'),
    path('product_rating', views.product_rating, name='product_rating'),
    path('customer_service_review', views.customer_service_review, name='customer_service_review'),

    path('view_cart', views.view_cart, name='view_cart'),
    path('product_quote', views.product_quote, name='product_quote'),
    path('checkout', views.checkout, name='checkout'),
    # path('sales_order', views.sales_order, name='sales_order'),
    # path('sales_order_tracking', views.sales_order_tracking, name='sales_order_tracking'),
    path('view_wishlist', views.view_wishlist, name='view_wishlist'),
    path('wishlist_add_to_cart', views.wishlist_add_to_cart, name='wishlist_add_to_cart'),
]


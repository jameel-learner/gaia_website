from django.urls import path
from . import views
app_name = 'product'

urlpatterns = [
    path('shop_by_category', views.shop_by_category, name='shop_by_category'),
    path('search_filter', views.search_filter, name='search_filter'),
    path('product_gallery', views.product_gallery, name='product_gallery'),
    path('recently_viewed', views.recently_viewed, name='recently_viewed'),

    path('product_detail', views.product_detail, name='product_detail'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('add_to_wishlist', views.add_to_wishlist, name='add_to_wishlist'),
]

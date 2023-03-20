from django.urls import path
from . import views
app_name = 'ui'

urlpatterns = [
    # path('', views.home, name='home'),
    path('contact_us/<slug:service_name>/', views.contact_us, name='contact_us'),
    path('about_us', views.about_us, name='about_us'),
    path('history_all', views.history_all, name='history_all'),
    path('history/<slug:service_name>/', views.history, name='history'),
    path('strategy', views.strategy, name='strategy'),
    path('md_message', views.md_message, name='md_message'),

    path('team/<slug:team_name>/', views.team, name='team'),
    path('business/<slug:service_name>/', views.business, name='business'),
    path('partnering/<slug:service_name>/', views.partnering, name='partnering'),
    path('shop', views.shop, name='shop'),
    path('media_all', views.media_all, name='media_all'),
    path('media/<slug:mtitle>/', views.media, name='media'),
    path('shop_all/<slug:category>/', views.shop_all, name='shop_all'),
    path('product/<int:pid>/<slug:product_name>/', views.product, name='product'),
]

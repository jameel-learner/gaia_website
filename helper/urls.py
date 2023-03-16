from django.urls import path
from . import views
app_name = 'helper'

urlpatterns = [
    path('get_captcha/', views.get_captcha, name='get_captcha'),
    path('get_code_word/', views.get_code_word, name='get_code_word'),
    path('get_vc_details/', views.get_vc_details, name='get_vc_details'),
    path('fetch_data/', views.fetch_data, name='fetch_data'),
    path('fetch_name_of_from/', views.fetch_name_of_from, name='fetch_name_of_from'),
]
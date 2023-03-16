from django.urls import path
from . import views
app_name = 'website'

urlpatterns = [
    # path('', views.home, name='home'),
    # path('contact_us', views.contact_us, name='contact_us'),
    path('search', views.search, name='search'),
    path('show_rfq_details/<int:rfq_id>/', views.show_rfq_details, name='show_rfq_details'),
    # path('about_us', views.about_us, name='about_us'),
    # path('services/<int:number>/', views.services, name='services'),
    # path('management', views.management, name='management'),
    # path('quality', views.quality, name='quality'),

]

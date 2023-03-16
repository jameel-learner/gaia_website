from django.urls import path
from . import views
app_name = 'cpanel'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('load_excel/', views.load_excel, name='load_excel'),
    path('reconcile/', views.reconcile, name='reconcile'),
]

"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ui.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('website/', include('website.urls')),
    path('ui/', include('ui.urls')),
    path('accounts/', include('accounts.urls')),
    path('business/', include('business.urls')),
    path('inventory/', include('inventory.urls')),
    path('logistic/', include('logistic.urls')),
    path('payment/', include('payment.urls')),
    path('product/', include('product.urls')),
    path('purchase/', include('purchase.urls')),
    path('sales/', include('sales.urls')),
    path('cpanel/', include('cpanel.urls')),
    path('helper/', include('helper.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'GAIA Healthcare Administration'                    # default: "Django Administration"
admin.site.site_title = 'GAIA Healthcare'
admin.site.index_title = 'GAIA Healthcare CPanel'                 # default: "Site administration"

handler404 = 'helper.views.handler404'
handler500 = 'helper.views.handler500'


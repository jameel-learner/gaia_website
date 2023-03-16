from django.contrib import admin
from accounts.models import *
# from masters.models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (_('Credentials'), {'fields': ('username', 'password', 'email', 'mobile_number', 'role', 'is_staff', 'groups', 'is_active')}),
    )
    list_display = ('username', 'mobile_number', 'email', )
    list_filter = ('groups__name', 'role',)
    search_fields = ('username', 'mobile_number', 'email', )


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserRole)

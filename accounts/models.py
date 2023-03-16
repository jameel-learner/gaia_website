from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# from common.models import BaseModel
import string
import random
from django.utils.translation import ugettext_lazy as _
import datetime
from django.db.models import F


# Create your models here.
class BaseModel(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserRole(BaseModel):
    name = models.CharField(max_length=50)
    role_permission = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name


class User(AbstractUser):
    ID = 'id'
    USERNAME = 'username'
    PASSWORD = 'password'
    EMAIL = 'email'
    MOBILE_NUMBER = 'mobile_number'
    IS_ACTIVE = 'is_active'
    ROLE = 'role'
    ADMIN = 'Admin'
    DONOR = 'Donor'
    VOLUNTEER = 'Volunteer'
    SAFEER = 'Safeer'

    email = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.CharField(max_length=50,blank=True, null=True)
    role = models.ManyToManyField(UserRole, related_name='get_users')
    encoded_pwd = models.CharField(max_length=100, blank=True, null=True)
    is_admin_access = models.BooleanField(default=False)
    register_type = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = _("Manage Members")
        verbose_name_plural = _("Manage Members")

    # def get_full_name(self):
    #     try:
    #         if self.last_name:
    #             return self.first_name + " " + self.last_name
    #         return self.first_name
    #     except:
    #         return ""

    # ADMIN_DASHBOARD = '/accounts/home/'
    ADMIN_DASHBOARD = '/accounts/two_step_mobile_verification/'
    DONOR_DASHBOARD = '/donation/donor_dashboard/'
    VOLUNTEER_DASHBOARD = '/'
    SAFEER_DASHBOARD = '/'
    # SAFEER_DASHBOARD = '/accounts/safeer_dashboard/'

    def get_dashboard_path(self):
        dashboard_path = User.VOLUNTEER_DASHBOARD
        if self.role.get().name == User.ADMIN:
            dashboard_path = User.ADMIN_DASHBOARD

        elif self.role.get().name == User.DONOR:
            dashboard_path = User.DONOR_DASHBOARD

        elif self.role.get().name == User.VOLUNTEER:
            if self.is_admin_access == True:
                dashboard_path = User.ADMIN_DASHBOARD
            elif self.is_staff == True:
                dashboard_path = User.ADMIN_DASHBOARD
            else:
                dashboard_path = User.VOLUNTEER_DASHBOARD

        elif self.role.get().name == User.SAFEER:
            if self.is_admin_access == True:
                dashboard_path = User.ADMIN_DASHBOARD
            else:
                dashboard_path = User.SAFEER_DASHBOARD

        return dashboard_path


def random_string_generator(size, include_lowercase=True, include_uppercase=True, include_number=True):
    s = ""
    if include_lowercase:
        s = s + string.ascii_lowercase
    if include_uppercase:
        s = s + string.ascii_uppercase
    if include_number:
        s = s + string.digits

    if len(s) > 0:
        s = ''.join(random.sample(s, len(s)))
        return ''.join(random.choice(s) for _ in range(size))


STATUS_TYPE = [('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Refunded', 'Refunded'),
               ('Pending', 'Pending')]


class VerifyMobileOtp(BaseModel):
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    otp_code = models.CharField(max_length=255, blank=True, null=True)
    max_count = models.IntegerField(blank=True, null=True, default=10)


from .models import User
from django.contrib.auth import get_user_model
from django.db.models import Q


class AuthBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False


    def get_user(self, user_id):
       try:
          return User.objects.get(pk=user_id)
       except User.DoesNotExist:
          return None

    def authenticate(self, username=None, password=None):
        mobile_number = None
        email = None
        try:
            mobile_number = int(username)
        except:
            email = username
        print(f'mobile_number: {mobile_number}   email: {email}')
        try:
            if mobile_number:
                user = User.objects.get(mobile_number=username)
            elif email:
                user = User.objects.get(username=username)

        except User.DoesNotExist:
            return None

        print(f'password: {password}   user: {user}')
        if password is None:
            return user if user else None
        return user if user.check_password(password) else None

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None

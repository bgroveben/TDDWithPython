from accounts.models import User, Token
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()


class PasswordlessAuthenticationBackend(object):


    def authenticate(self, uid):
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None


    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

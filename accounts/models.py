import uuid
from django.contrib import auth
from django.db import models

# Django's authentication framework expects the user model to have a last_login field
auth.signals.user_logged_in.disconnect(auth.models.update_last_login)


class User(models.Model):
    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = ()
    USERNAME_FIELD = 'email'


    def is_authenticated(self):
        try:
            return self.email
        except User.DoesNotExist:
            return None


class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(default=uuid.uuid4, max_length=40)

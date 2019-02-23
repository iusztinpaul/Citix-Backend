from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _


class CloudGeneratedToken(Token):
    refresh_key = models.CharField(_("Refresh Key"), max_length=40, null=True, blank=True)

    def generate_key(self):
        # The key will be generated by the cloud and persisted on signup/login.
        return self.user.auth_token.key


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('phone_number'), max_length=255, blank=True, null=True)

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

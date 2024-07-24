import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "vinipoonpn.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import vinipoonpn.users.signals  # noqa: F401

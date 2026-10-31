import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class StrongPasswordValidator:
    """More than 8 characters, with uppercase, lowercase and a special character."""

    def validate(self, password, user=None):
        errors = []
        if len(password) <= 8:
            errors.append(_("Password must be more than 8 characters."))
        if not re.search(r"[A-Z]", password):
            errors.append(_("Password must contain an uppercase letter."))
        if not re.search(r"[a-z]", password):
            errors.append(_("Password must contain a lowercase letter."))
        if not re.search(r"[^A-Za-z0-9]", password):
            errors.append(_("Password must contain a special character."))
        if errors:
            raise ValidationError(errors)

    def get_help_text(self):
        return _(
            "Your password must be more than 8 characters and contain "
            "an uppercase letter, a lowercase letter and a special character."
        )

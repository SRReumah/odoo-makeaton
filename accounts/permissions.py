from functools import wraps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

# USAGE (send to teammates):
# from accounts.permissions import role_required, RoleRequiredMixin, OwnershipMixin
# @role_required(["admin", "staff"])   -> on a function view
# class X(RoleRequiredMixin, ListView): allowed_roles = ["admin", "staff"]
# class MySubs(OwnershipMixin, ListView): model = Subscription  (uses owner_field = "customer")
# if customer points to a profile, set owner_field = "customer__user"


def is_admin(user):
    return user.is_superuser or getattr(user, "role", "") == "admin"


def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("login")
            if not is_admin(request.user) and request.user.role not in allowed_roles:
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return wrapped
    return decorator


class RoleRequiredMixin(LoginRequiredMixin):
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not is_admin(request.user) and request.user.role not in self.allowed_roles:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class OwnershipMixin(LoginRequiredMixin):
    owner_field = "customer"

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if is_admin(user) or user.role == "staff":
            return qs
        return qs.filter(**{self.owner_field: user})

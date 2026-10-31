from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("create-staff/", views.create_staff, name="create_staff"),
    path("staff-only/", views.staff_only, name="staff_only"),
    path("customer-only/", views.customer_only, name="customer_only"),
]

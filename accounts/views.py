from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, StaffCreationForm
from .permissions import role_required


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


@login_required
def home(request):
    return HttpResponse(f"Logged in as {request.user.email}. Role: {request.user.role}")


@role_required(["admin"])
def create_staff(request):
    if request.method == "POST":
        form = StaffCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Staff member created successfully! <a href='/'>Go Home</a>")
    else:
        form = StaffCreationForm()
    return render(request, "accounts/signup.html", {"form": form, "title": "Create Staff Member"})


@role_required(["admin", "staff"])
def staff_only(request):
    return HttpResponse("Welcome, Staff or Admin. Customers cannot see this page.")


@role_required(["customer"])
def customer_only(request):
    return HttpResponse("Welcome, Customer. Staff and Admin cannot see this page.")

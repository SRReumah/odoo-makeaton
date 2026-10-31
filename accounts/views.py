from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import SignupForm


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


def home(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Logged in as {request.user.email}")
    return HttpResponse("Not logged in")

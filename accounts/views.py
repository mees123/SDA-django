from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignUpForm


class CustomizedLoginView(LoginView):
    template_name = "accounts/login.html"


class CustomizedPasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def from_valid(self, form):
        messages.success(
            self.request,
            "New Account Created!",
            extra_tags="btn-success"
        )

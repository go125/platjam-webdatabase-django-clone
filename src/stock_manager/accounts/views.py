from django.shortcuts import render
from django.contrib.auth.views import LoginView
from accounts.forms import LoginForm

class MyLoginView(LoginView):
    form_class = LoginForm

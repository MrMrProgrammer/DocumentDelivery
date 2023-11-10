from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from .forms import LoginForm
from django.contrib.auth.models import AbstractUser
from django.http import HttpRequest


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class LoginView(View):
    def get(self, request):

        login_form = LoginForm()

        context = {
            'login_form': login_form
        }

        return render(request, 'User/login.html', context)

    def post(self, request: HttpRequest):

        login_form = LoginForm(request.POST)

        if login_form.is_valid():

            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user: AbstractUser = AbstractUser.objects.filter(email__iexact=username).first()

            if user is not None:
                is_password_correct = user.check_password(password)

                if is_password_correct:
                    login(request, user)

                    return redirect('show-store')

                else:
                    login_form.add_error('password', 'ایمیل یا رمز عبور اشتباه است (رمز عبور)')

            else:
                login_form.add_error('username', 'ایمیل یا رمز عبور اشتباه است (نام کاربری)')

        context = {
            'login_form': login_form
        }

        return render(request, 'User/login.html', context)

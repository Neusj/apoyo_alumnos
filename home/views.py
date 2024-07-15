from django import views
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, PasswordResetView
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordResetForm


class Home(views.View):
    def get(self, request):
        return render(
            request,
            'home.html',
            {
                'message': 'Nueva plataforma de apoyo al estudiante'
            }
        )


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'password_reset.html'
    success_url = '/login/'

from django import views
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, PasswordResetView
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordResetForm
from django.contrib.auth.mixins import UserPassesTestMixin


class Home(views.View):
    def get(self, request):
        user = request.user
        message = 'Nueva plataforma de apoyo al estudiante'
        is_login = False
        if user.is_authenticated:
            message = f'¡Hola! {user.username}'
            is_login = True

        return render(
            request,
            'home.html',
            {
                'message': message,
                'is_login': is_login
            }
        )


class SignUpView(UserPassesTestMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
    def test_func(self):
        return self.request.user.tipo == 'administrador'

    def handle_no_permission(self):
        return redirect('home')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'password_reset.html'
    success_url = '/login/'

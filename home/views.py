from django import views
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test

from home.models import CustomUser
from home.utils.utils import is_administrador
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordResetForm
from django.contrib.auth.mixins import UserPassesTestMixin


class Home(views.View):
    def get(self, request):
        user = request.user
        message = 'Nueva plataforma de apoyo al usuario'
        is_login = False
        if user.is_authenticated:
            message = f'¡Hola! {user.first_name} {user.last_name}'
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


@user_passes_test(is_administrador, login_url='home')
def usuario_list(request):
    usuarios = CustomUser.objects.all()
    return render(request, 'usuario_list.html', {'usuarios': usuarios})

@user_passes_test(is_administrador, login_url='home')
def usuario_update(request, pk):
    usuario = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = CustomUserCreationForm(instance=usuario)
    return render(request, 'signup.html', {'form': form, 'edit_view': True})

def usuario_delete(request, pk):
    usuario = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuario_confirm_delete.html', {'usuario': usuario})


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'password_reset.html'
    success_url = '/login/'

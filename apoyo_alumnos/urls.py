"""apoyo_alumnos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
from area_estudiante.views import curso_create, curso_delete, curso_list, curso_update, estudiante_create, estudiante_delete, estudiante_list, estudiante_update, tipo_conducta_create, tipo_conducta_delete, tipo_conducta_list, tipo_conducta_update
from home.views import CustomLoginView, CustomPasswordResetView, Home, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),

    path('crear_usuario/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),

    # Curso
    path('cursos/', curso_list, name='curso_list'),
    path('cursos/create/', curso_create, name='curso_create'),
    path('cursos/update/<int:pk>/', curso_update, name='curso_update'),
    path('cursos/delete/<int:pk>/', curso_delete, name='curso_delete'),

    # TipoConducta
    path('tipo_conductas/', tipo_conducta_list, name='tipo_conducta_list'),
    path('tipo_conductas/create/', tipo_conducta_create, name='tipo_conducta_create'),
    path('tipo_conductas/update/<int:pk>/', tipo_conducta_update, name='tipo_conducta_update'),
    path('tipo_conductas/delete/<int:pk>/', tipo_conducta_delete, name='tipo_conducta_delete'),

    # Estudiante
    path('estudiantes/', estudiante_list, name='estudiante_list'),
    path('estudiantes/create/', estudiante_create, name='estudiante_create'),
    path('estudiantes/update/<int:pk>/', estudiante_update, name='estudiante_update'),
    path('estudiantes/delete/<int:pk>/', estudiante_delete, name='estudiante_delete'),

]

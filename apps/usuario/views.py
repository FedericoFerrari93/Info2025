from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .forms import RegistroUsuarioForm

class RegistroUsuario(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('apps.usuario:login') # Redirige al login tras registrarse

class Login(auth_views.LoginView):
    template_name = 'usuarios/login.html'
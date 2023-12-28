from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.decorators import method_decorator
from album.models import Album

def home(request):
    data = Album.objects.all()
    return render(request, 'home.html', {'data':data})


class user_signup(CreateView):
    form_class = RegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signup')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Sign Up Successfully')
        return response




class user_login(LoginView):
    template_name = 'login.html'
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Logged In Successfully')
        return response
    def get_success_url(self):
        return reverse_lazy('home')



@method_decorator(login_required, name='dispatch')
class user_logout(LogoutView):
    def get_success_url(self):
        messages.success(self.request, 'Logged Out Successfully')
        return reverse_lazy('login')
        
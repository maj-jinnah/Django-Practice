from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def home(request):
    return render(request, 'home.html')

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save()
        else:
            form = UserRegistrationForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('login')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpassword = form.cleaned_data['password']
                user = authenticate(username=name, password=userpassword)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully')
                    return redirect('profile')
            
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('home') 

def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'password_change.html', {'form': form})
    else:
        return redirect('login')
    

def password_change_wp(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'password_change.html', {'form': form})
    else:
        return redirect('login')
    
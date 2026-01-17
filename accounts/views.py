from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import AdminSignupForm


def admin_signup(request):
    # if User.objects.filter(is_staff=True).exists():
    #     messages.error(request, "Admin account already exists.")
    #     return redirect('accounts:login')
    
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            user.is_staff = True
            user.is_superuser = False
            user.save()


            messages.success(request, "Admin account created successfully.")
            login(request, user)
            return redirect('/dashboard/')
    else:
        form = AdminSignupForm()

        return render(request, 'accounts/signup.html', {'form': form})
    

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request, "Invalid credentials or not an admin user.")
            return redirect('accounts:login')
    return render(request, 'accounts/login.html')


def admin_logout(request):
    logout(request)
    return redirect('/')
            

# Create your views here.

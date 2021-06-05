from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def Index(request):
    if request.user.is_authenticated:
        return redirect('main-dashboard')
    else:
        return render(request, 'index.html')


def Login(request):
    if request.user.is_authenticated:
        return redirect('main-dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main-dashboard')
            else:
                messages.warning(request, 'Invalid Username or Password!!!')

    return render(request, 'user/login.html')


def Register(request):
    if request.user.is_authenticated:
        return redirect('main-dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            first_name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            password1 = request.POST.get('password2')

            if password == password1:
                User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
            else:
                messages.error(request, 'Passwords did not match or invalid password!!!')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main-dashboard')

    return render(request, 'user/register.html')


@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('index')

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from accounts.forms import UserLoginForm, UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You registered successfully, now log in')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})


# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'you logged in successfully')
#                 return redirect('story:home')
#             else:
#                 messages.error(request, 'wrong username or password')
#     else:
#         form = UserLoginForm()
#     return render(request, 'accounts/login.html', {'form':form})
#
#
# @login_required
# def user_logout(request):
#     logout(request)
#     messages.success(request, 'you logged out successfully')
#     return redirect('story:home')
#
#
# def user_register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = User.objects.create_user(cd['username'], cd['email'], cd['password1'])
#             login(request, user)
#             messages.success(request, 'you registered successfully')
#             return redirect('story:home')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'accounts/register.html', {'form':form})
#

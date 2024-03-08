#type:ignore

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseNotFound

from belanjainaja.models import *

def index(request):
    return render(request, "projects.html")

def signin(request):

    if request.user.is_authenticated:
        return redirect("belanja:index")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("belanja:index")
        else:
            messages.add_message(request, messages.ERROR, "Username atau Password salah.")

    return render(request, "signin.html")

def signout(request):

    if request.method == "POST":
        logout(request)
        return redirect("belanja:index")
    
    return HttpResponseNotFound()

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.add_message(request, messages.SUCCESS, f'Berhasil registrasi dengan email {email}')
        except Exception as err:
            messages.add_message(request, messages.ERROR, err)

    return render(request, "register.html")
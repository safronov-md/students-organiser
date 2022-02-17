from django.shortcuts import render, redirect
from django.contrib.auth import authenticate


def login(request):
    return render(request, 'auth/login.html')


def auth(request):
    data = request.POST
    email = data.get('inputEmail')
    password = data.get('inputPassword')
    user = authenticate(email=email, password=password)
    print(user)
    if not user:
        return redirect('login')
    else:
        return redirect('calendar')


def register(request):
    return render(request, 'auth/register.html')

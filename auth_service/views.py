from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as login2, logout as logout2
from django.contrib.auth.hashers import make_password


def login(request):
    return render(request, 'auth/login.html')


def logout(request):
    if request.user.is_authenticated:
        logout2(request)
        return redirect('login')
    else:
        return redirect('calendar')


def auth(request):
    data = request.POST
    username = data.get('username')
    password = data.get('password')
    User = get_user_model()
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('login')
    else:
        if user.check_password(password):
            user = authenticate(username=username, password=password)
            login2(request=request, user=user)
            return redirect('calendar')
    return redirect('login')


def signup(request):
    data = request.POST
    pwd: str = str()
    if data.get('pwd') == data.get('pwd2'):
        pwd = make_password(data.get('pwd'))
    else:
        return redirect('register')
    User = get_user_model()
    if User.objects.filter(email=data.get('email')).exists():
        return redirect('register')
    if User.objects.filter(username=data.get('username')).exists():
        return redirect('register')
    regUser = User(
        username=data.get('username'),
        email=data.get('email'),
        password=pwd,
        first_name=data.get('first'),
        last_name=data.get('last'),
    )
    regUser.save()
    return redirect('login')


def register(request):
    return render(request, 'auth/register.html')

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.hashers import make_password


def login_view(request):
    return render(request, 'login.html')


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login_view')


def sign_in(request):
    data = request.POST
    email = data.get('email')
    password = data.get('password')
    User = get_user_model()
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return redirect('login_view')
    else:
        if user.check_password(password):
            login(request=request, user=user)
            return redirect('dashboard_view')
    return redirect('login_view')


def sign_up(request):
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


def sign_up_view(request):
    return render(request, 'register.html')

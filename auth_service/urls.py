from django.urls import path
from auth_service.views import login_view, sign_out, sign_up_view, sign_in

urlpatterns = [
    path('login', login_view, name="login_view"),
    path('sign_in', sign_in, name="sign_in_function"),
    path('logout', sign_out, name="logout"),
    path('signup', sign_up_view, name="sign_up_view"),
]

from django import forms
from django.contrib.auth import authenticate, get_user_model


class UserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("This User doesn't exist")
            if not user.check_password(password):
                raise forms.ValidationError("Wrong password!")
            if not user.is_active:
                raise forms.ValidationError("Inactive user!")
        return super(UserLoginForm, self)

from django.core import validators
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation


class NewUserForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password', 'id': 'passl', 'data-type': 'password',
                                          'placeholder': 'Enter Password'}))
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password', 'id': 'passl', 'data-type': 'password',
                                          'placeholder': 'Enter Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'type': 'text', 'id': 'userl', 'placeholder': 'Enter UserName'})}


# 		if commit:
# 			user.save()
# 		return user

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'input', 'id': 'userl', 'type': 'text',
               'placeholder': 'Enter UserName'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'input', 'data-type': 'password', 'id': 'passl',
               'placeholder': 'Enter Your Password'}))

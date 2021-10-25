from django.core import validators
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation


class NewUserForm(UserCreationForm):
    password1 = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
            attrs={'class': 'input', 'type': 'password', 'id': 'passr1', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(
            attrs={'class': 'input', 'type': 'password', 'id': 'passr2', 'placeholder': 'Enter Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'id': 'userr1', 'placeholder': 'Enter UserName'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'input', 'id': 'userl1', 'type': 'text',
               'placeholder': 'Enter UserName'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'input', 'type': 'password', 'id': 'passl1',
               'placeholder': 'Enter Your Password'}))


class FilterForm(forms.Form):
    date1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'dateFrom', 'type': 'date'}))
    date2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'dateTo', 'type': 'date'}))


class EditForm(forms.Form):
    bs = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    pbsq = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    ptsq = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    psqs = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    pbsc = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    psgc = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    pbnc = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    sld = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    sdl = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    oss = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    ac = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    tsequence = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    sqlenth = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    gc = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    lane = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))
    row = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'id': 'editform', 'type': 'text'}))

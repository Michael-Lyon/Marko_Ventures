from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreationUserForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form2__input',
        'type': "text",
        'placeholder': "Username",
        'id': "uname"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'class': 'form2__input',
        'type': "email",
        'placeholder': "Email  address",
        'id': "email"}))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form2__input',
        'type': "password",
        'placeholder': "Password",
        'id': "pass"}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form2__input',
        'type': "password",
        'placeholder': "Re-enter password",
        'id': "pass2"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

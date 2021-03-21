from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UploadRecordForm(forms.ModelForm):
    class Meta:
        fields = ("image", )
        model = Record


class ChangePhotoForm(forms.Form):
    image = forms.ImageField()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
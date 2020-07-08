from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.db import models

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    your_name = forms.CharField(label='Full Name:', max_length=100)
    
    # no_of_images_uploaded = models.IntegerField(default=0)
    # download_image_today = models.IntegerField(default=0)

    class Meta:
        model = User
        fields = ["username", "your_name", "email", "password1", "password2"]



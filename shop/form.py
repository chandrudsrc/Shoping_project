from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the username'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter the password','id':'psw'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter the Confirm Password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password_confirm = forms.CharField(max_length=200, widget=forms.PasswordInput())
    field_order=['username', 'password', 'password_confirm', 'email']

    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = ['username', 'password', 'email']

class LoginForm(forms.Form):
    #modelForm -> form 
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
   
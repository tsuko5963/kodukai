from django import forms
from django.contrib.auth.models import User

class AccountForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(), label = "パスワード")

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        labels = {'username':"ユーザーID", 'email':"メール"}


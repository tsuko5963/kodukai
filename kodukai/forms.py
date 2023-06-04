from django import forms
from django.contrib.auth.models import User
from .models import Treasurer

class AccountForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(), label = "パスワード")

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        labels = {'username':"ユーザーID", 'email':"メール"}

class RecordForm(forms.ModelForm):
    user = forms.CharField(widget = forms.HiddenInput())

    class Meta():
        model = Treasurer
        fields = ('use_date', 'item', 'debit', 'credit', 'amount', 'user')
        labels = {'use_data':'使用日', 'item':'用途', 'debit':'借方', 'credit':'貸方', 'amount':'金額', 'user':'ユーザ名'}


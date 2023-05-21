from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from .forms import AccountForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method == 'POST':
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')
        user = authenticate(username = ID, password = Pass)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("アカウントが有効ではありません")
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        else:    
            return render(request, 'kodukai/login.html')

@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login'))

@login_required
def home(request):
    params = {"UserID": request.user,}
    return render(request, "kodukai/home.html", context = params)

@login_required
def Register(request):
    params = {
        "AccountCreate":False,
        "account_form":AccountForm(),
    }
    if request.method == 'POST':
        params["account_form"] = AccountForm(data = request.POST)
    
        if params["account_form"].is_valid():
            account = params["account_form"].save()
            account.set_password(account.password)
            account.save()
    
            params["AccountCreate"] = True
        else:
            print(params["account_form"].errors)
    
        return render(request, "kodukai/register.html", context = params)
    else:
        params["account_form"] = AccountForm()
        params["AccountCreate"] = False
        return render(request, "kodukai/register.html", context = params)

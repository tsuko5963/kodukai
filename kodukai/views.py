from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

from django.views.generic import TemplateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AccountForm, RecordForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Treasurer, ValidDate
from datetime import date, timedelta
import datetime

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
    params = {"UserID": request.user}
    start_date = ValidDate.objects.get(key=1).valid_date
    dt_32 = datetime.timedelta(days=32)
    dt_1 = datetime.timedelta(days=1)
    end_date = start_date + dt_32
    end_date = date(end_date.year, end_date.month, 1) - dt_1
    treasurer = Treasurer.objects.filter(use_date__range=[start_date,end_date]).values()
    b = 0
    c = 0
    d = 0
    g = 0
    k = 0
    s = 0
    t = 0
    u = 0
    p = 0
    for row in treasurer:
        if row['debit'] == 'b':
            b = b + row['amount']
        if row['debit'] == 'c':
            c = c - row['amount']
        if row['debit'] == 'd':
            d = d - row['amount']
        if row['debit'] == 'g':
            g = g + row['amount']
        if row['debit'] == 'k':
            k = k - row['amount']
        if row['debit'] == 's':
            s = s + row['amount']
        if row['debit'] == 't':
            t = t + row['amount']
        if row['debit'] == 'u':
            u = u - row['amount']
        if row['debit'] == 'p':
            p = p + row['amount']
        if row['credit'] == 'b':
            b = b - row['amount']
        if row['credit'] == 'c':
            c = c + row['amount']
        if row['credit'] == 'd':
            d = d + row['amount']
        if row['credit'] == 'g':
            g = g - row['amount']
        if row['credit'] == 'k':
            k = k + row['amount']
        if row['credit'] == 's':
            s = s - row['amount']
        if row['credit'] == 't':
            t = t - row['amount']
        if row['credit'] == 'u':
            u = u + row['amount']
        if row['credit'] == 'p':
            p = p - row['amount']
    params["b"] = b 
    params["c"] = c 
    params["d"] = d 
    params["g"] = g 
    params["k"] = k 
    params["s"] = s 
    params["t"] = t 
    params["u"] = u 
    params["p"] = p 
    return render(request, "kodukai/home.html", context = params)

@login_required
def register(request):
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

@login_required
def insert(request):
    params = {}
    if request.method == 'POST':
        params['record_form'] = RecordForm(data = request.POST)
        if params['record_form'].is_valid(): 
            record = params['record_form'].save()
            record.save()
            params['RecordCreate'] = True
        else:
            print(params["record_form"].errors)
        return render(request, "kodukai/insert.html", context = params)
    else:
        d = datetime.datetime.today().date()
        fields = ('use_date', 'item', 'debit', 'credit', 'amount')
        initial_dict = dict(use_date = d, amount = 0)
        params["record_form"] = RecordForm(data = initial_dict)
        params["RecordCreate"] = False
        return render(request, "kodukai/insert.html", context = params)

class RecordIndexView(LoginRequiredMixin, ListView):
    template_name = "kodukai/list.html"
    context_object_name = 'latest_treasurer_list'
    
    def get_queryset(self):
        start_date = ValidDate.objects.get(key=1).valid_date
        dt_32 = datetime.timedelta(days=32)
        dt_1 = datetime.timedelta(days=1)
        end_date = start_date + dt_32
        end_date = date(end_date.year, end_date.month, 1) - dt_1
        return Treasurer.objects.filter(use_date__range=[start_date,end_date]).order_by("use_date")

@login_required
def detail_view(request, record_id):
    treasurer = get_object_or_404(Treasurer, pk = record_id)
    return render(request, 'kodukai/detail.html', {'treasurer': treasurer})

@login_required
def edit_view(request, record_id):
    treasurer = get_object_or_404(Treasurer, pk = record_id)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance = treasurer)
        if form.is_valid():
            form.save()
            return redirect('detail_view', record_id = record_id)
    else:
        form = RecordForm(instance = treasurer)
    return render(request, 'kodukai/edit.html', {'form': form})

class RecordDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'kodukai/delete.html'
    model = Treasurer
    success_url = reverse_lazy('List')


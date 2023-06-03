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
        if row['debit'] == '銀行':
            b = b + row['amount']
        if row['debit'] == 'カード':
            c = c - row['amount']
        if row['debit'] == '借金':
            d = d - row['amount']
        if row['debit'] == '現金':
            g = g + row['amount']
        if row['debit'] == '費用':
            k = k - row['amount']
        if row['debit'] == 'スイカ':
            s = s + row['amount']
        if row['debit'] == '立替':
            t = t + row['amount']
        if row['debit'] == '引当金':
            u = u - row['amount']
        if row['debit'] == 'ペイペイ':
            p = p + row['amount']
        if row['credit'] == '銀行':
            b = b - row['amount']
        if row['credit'] == 'カード':
            c = c + row['amount']
        if row['credit'] == '借金':
            d = d + row['amount']
        if row['credit'] == '現金':
            g = g - row['amount']
        if row['credit'] == '収入':
            k = k + row['amount']
        if row['credit'] == 'スイカ':
            s = s - row['amount']
        if row['credit'] == '立替':
            t = t - row['amount']
        if row['credit'] == '引当金':
            u = u + row['amount']
        if row['credit'] == 'ペイペイ':
            p = p - row['amount']
    params["銀行"] = b 
    params["カード"] = c 
    params["借金"] = d 
    params["現金"] = g 
    params["小遣い"] = k 
    params["スイカ"] = s 
    params["立替"] = t 
    params["引当金"] = u 
    params["ペイペイ"] = p 
    params["年"] = start_date.year 
    params["月"] = start_date.month 
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
        d = ValidDate.objects.get(key=1).valid_date
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
def close_month(request):
    if request.method == 'POST':
        start_date = ValidDate.objects.get(key=1).valid_date
        dt_32 = datetime.timedelta(days=32)
        dt_1 = datetime.timedelta(days=1)
        end_date = start_date + dt_32
        new_date = date(end_date.year, end_date.month, 1)
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
            if row['debit'] == '銀行':
                b = b + row['amount']
            if row['debit'] == 'カード':
                c = c - row['amount']
            if row['debit'] == '借金':
                d = d - row['amount']
            if row['debit'] == '現金':
                g = g + row['amount']
            if row['debit'] == '費用':
                k = k - row['amount']
            if row['debit'] == 'スイカ':
                s = s + row['amount']
            if row['debit'] == '立替':
                t = t + row['amount']
            if row['debit'] == '引当金':
                u = u - row['amount']
            if row['debit'] == 'ペイペイ':
                p = p + row['amount']
            if row['credit'] == '銀行':
                b = b - row['amount']
            if row['credit'] == 'カード':
                c = c + row['amount']
            if row['credit'] == '借金':
                d = d + row['amount']
            if row['credit'] == '現金':
                g = g - row['amount']
            if row['credit'] == '収入':
                k = k + row['amount']
            if row['credit'] == 'スイカ':
                s = s - row['amount']
            if row['credit'] == '立替':
                t = t - row['amount']
            if row['credit'] == '引当金':
                u = u + row['amount']
            if row['credit'] == 'ペイペイ':
                p = p - row['amount']
        record = Treasurer(use_date = new_date, item = '繰越', debit = '銀行', credit = 'ダミー', amount = b)
        record.save()
        record = Treasurer(use_date = new_date, item = '繰越', debit = 'ダミー', credit = 'カード', amount = c)
        record.save()
        record = Treasurer(use_date = new_date, item = '繰越', debit = 'ダミー', credit = '借金', amount = d)
        record.save()
        record = Treasurer(use_date = new_date, item = '繰越', debit = '現金', credit = 'ダミー', amount = g)
        record.save()
        record = Treasurer(use_date = new_date, item = '繰越', debit = 'ダミー', credit = '収入', amount = k)
        record.save()
        record = Treasurer(use_date = new_date, item = '繰越', debit = 'スイカ', credit = 'ダミー', amount = s)
        record.save()
        record = Treasurer(use_date = new_date, item = '繰越', debit = '立替', credit = 'ダミー', amount = t)
        record.save()
        record = Treasurer(use_date = new_date, item = '繰越', debit = 'ダミー', credit = '引当金', amount = u)
        record.save()
        record = Treasurer(use_date = new_date, item = '繰越', debit = 'ペイペイ', credit = 'ダミー', amount = p)
        record.save()
        valid_date = ValidDate.objects.get(key=1)
        valid_date.valid_date = new_date
        valid_date.save()
        return redirect('home')
    else:
        return render(request, 'kodukai/close.html')

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


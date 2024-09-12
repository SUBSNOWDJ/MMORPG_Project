import datetime
import random
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from .models import OneTimeCode
from .forms import OTCodeForm, UserForm, LoginForm


def registration_view(request):
    form = UserForm()
    if request.POST.get('send'):
        form = UserForm(request.POST)
        if form.is_valid():
            # user = User.objects.create_user(email=form.email, username=form.username, password=form.password)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            exp_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
            code = OneTimeCode.objects.create(code=random.randint(100000, 999999), username=username, email=email,
                                              password=password, expire_time=exp_time)
            code.save()
            # post_save.connect(send_code, sender=OneTimeCode)
            return HttpResponseRedirect('/auth/code/')
        else:
            form = UserForm(request.POST)
            return render(request, 'registration.html', {'form': form, })
    return render(request, 'registration.html', {'form': form, })


def code_conformation_view(request):
    if request.method == 'POST':
        form = OTCodeForm(request.POST)
        if OneTimeCode.objects.filter(code=form.data['code']).exists():
            code_data = OneTimeCode.objects.filter(code=form.data['code'])
            for dat in code_data:
                user = User.objects.create_user(username=dat.username, email=dat.email, password=dat.password)
                user.save()
                dat.delete()
            return HttpResponseRedirect('/auth/login/')
    else:
        form = OTCodeForm()
        context = {'form': form, }
        return render(request, 'code.html', context)


def login_view(request):
    if request.POST.get('login'):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                form = LoginForm()
                error = 'wrong username or password'
                context = {'form': form, 'error': error, }
                return render(request, 'login.html', context)
    if request.POST.get('registration'):
        return HttpResponseRedirect('/auth/registration/')
    form = LoginForm()
    context = {'form': form, }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

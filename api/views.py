from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from api.forms import LoginForm, NewUserForm
from zipfile import ZipFile
import os
import time
import re
from os import listdir
from os.path import isfile, join
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CustomerRegView(View):
    def get(self, request):
        form1 = LoginForm()
        form2 = NewUserForm()
        return render(request, 'login_regis.html', {'login_form': form1, 'register_form': form2})

    def post(self, request):
        if request.method == "POST":
            if request.POST.get('signup'):
                form = NewUserForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    login(request, user)
                    messages.success(request, "Registration successful." )
                    return redirect('login')
                messages.error(request, "Unsuccessful registration. Invalid information.")
                form = NewUserForm()
                return render (request, 'login_regis.html', {'register_form':form})

            if request.POST.get('signin'):
                form = LoginForm(request, data=request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.info(request, f"You are now logged in as {username}.")
                        return redirect('home')
                    else:
                        messages.error(request,"Invalid username or password.")
                else:
                    messages.error(request,"Invalid username or password.")
                form = LoginForm()
                return render(request, 'login_regis.html', {'login_form': form})



def home(request):
    HOME_FOLDER = 'E:/Python Program/FolderPro/api/static/zipfiles'
    dirfiles = os.listdir(HOME_FOLDER)
    fullpaths = map(lambda name: os.path.join(HOME_FOLDER, name), dirfiles)

    dirs = []
    files = []
    data = []
    for file in fullpaths:
        if os.path.isdir(file): dirs.append(file)
        if os.path.isfile(file): files.append(file)

    x = list(dirs)
    for i in x:
        sep = i.split('_')
        res = []
        name = ['Sample_name', 'True_Sequence', 'Flowcell', 'Lane', 'Rack', 'Fastqc', 'Date']
        path_time = os.path.getctime(i)
        c_ti = time.ctime(path_time)
        sep.append(c_ti)
        dictfile = zip(name, sep)
        newdict = dict(dictfile)
        for ele in sep:
            res.append(ele.split('\\'))
        data.append(newdict)

    # page = request.GET.get('page', 1)

    # paginator = Paginator(data)
    # try:
    #     users = paginator.page(page)
    # except PageNotAnInteger:
    #     users = paginator.page(1)
    # except EmptyPage:
    #     users = paginator.page(paginator.num_pages)       
    return render(request, 'profile.html', {'data': data})
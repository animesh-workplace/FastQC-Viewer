from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from api.forms import LoginForm, NewUserForm
from zipfile import ZipFile
import os
import glob
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
                    form1 = LoginForm()
                    messages.success(request, "Registration successful.")
                    return redirect('login')
                messages.error(request, "Unsuccessful registration. Invalid information.")
                form = NewUserForm()
                return render(request, 'login_regis.html', {'register_form': form})

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
                        messages.error(request, "Invalid username or password.")
                else:
                    messages.error(request, "Invalid username or password.")
                form = LoginForm()
                return render(request, 'login_regis.html', {'login_form': form})

@login_required()
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
        os.chdir(i)
        text_file = glob.glob('*.txt')
        image_path = i.split('\\')
        sam = image_path[1].split('_')
        name = ['Sample_name', 'True_Sequence', 'Flowcell', 'Lane', 'Rack', 'Fastqc', 'Date', 'Path',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        path_time = os.path.getctime(i)
        c_ti = time.ctime(path_time)
        sam.append(c_ti)
        sam.append(image_path[1])
        # print(text_file[1])
        for f in text_file:
            outfile = open(f, 'r')
            read_file = outfile.read().split()
            outfile.close()
            # print(read_file)
        sam.append(read_file[0])
        sam.append(read_file[4])
        sam.append(read_file[10])
        sam.append(read_file[16])
        sam.append(read_file[22])
        sam.append(read_file[28])
        sam.append(read_file[34])
        sam.append(read_file[40])
        sam.append(read_file[45])
        sam.append(read_file[50])
        sam.append(read_file[54])
        dictfile = zip(name, sam)
        newdict = dict(dictfile)
        data.append(newdict)
    print(" New Data ", data)    
    return render(request, 'profile.html', {'data': data})

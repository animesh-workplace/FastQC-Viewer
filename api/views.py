from django.db.models import Q, Count, Max
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from api.forms import LoginForm, NewUserForm, FilterForm
from backend.settings import BASE_DIR, MEDIA_URL
from .models import ProjectTable, Data1, Data2
from zipfile import ZipFile
import os
import glob
import time
import re
from os import listdir
from os.path import isfile, join


# Main Code

# path_file = os.path.join(BASE_DIR / 'media/project')
# dirfiles = os.listdir(path_file)
# fullpaths = map(lambda name: os.path.join(path_file, name), dirfiles)
# dirs = []
# data = []
# for file in fullpaths:
#     if os.path.isdir(file): dirs.append(file)
#     os.getcwd()
# x = list(dirs)
# path_list = []
# for i in x:
#     all_path = []
#     root_path = []
#     for root, dirs, files, in os.walk(i):
#         all_path.append(root)
#     path_list.append(all_path[2])
#     path_list.append(all_path[25])
#
# for j in path_list:
#     folder_path = os.listdir(j)
#     folder_list = map(lambda name: os.path.join(j, name), folder_path)
#     fl = []
#     for folder in folder_list:
#         if os.path.isdir(folder): fl.append(folder)
#         os.getcwd()
#     y = list(fl)
#
#     for o in y:
#         os.chdir(o)
#         text_file = glob.glob('*.txt')
#         image_path = o.split('\\')
#         new_split = image_path[8].split('_')
#         name = ['a', 'b', 'c', 'd', 'e', 'Project_name', 'Sub_folder', 'fastqc', 'Path', 'Date', 'Sample_name',
#                 'TrueSq', 'Flowcell', 'Lane', 'Row', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
#                 '11', 'Total_Sequence', 'Lenth', 'GC']
#         path_time = os.path.getatime(o)
#         c_ti = time.ctime(path_time)
#         t_obj = time.strptime(c_ti)
#         T_stamp = time.strftime("%d-%m-%Y %H:%M:%S", t_obj)
#
#         image_path.append(T_stamp[0:10])
#
#         with open(text_file[0], 'r') as f1, open(text_file[1], 'r') as f2:
#             read_file = f2.read().split()
#             fastqc_file = f1.read().split()
#
#         image_path.append(new_split[0])
#         image_path.append(new_split[1])
#         image_path.append(new_split[2])
#         image_path.append(new_split[3])
#         image_path.append(new_split[4])
#         image_path.append(read_file[0])
#         image_path.append(read_file[4])
#         image_path.append(read_file[10])
#         image_path.append(read_file[16])
#         image_path.append(read_file[22])
#         image_path.append(read_file[28])
#         image_path.append(read_file[34])
#         image_path.append(read_file[40])
#         image_path.append(read_file[45])
#         image_path.append(read_file[50])
#         image_path.append(read_file[54])
#         image_path.append(fastqc_file[21])
#         image_path.append(fastqc_file[30])
#         image_path.append(fastqc_file[32])
#         dictfile = zip(name, image_path)
#         newdict = dict(dictfile)
#         data.append(newdict)

# path_file = os.path.join(BASE_DIR / 'media/project')
# dirfiles = os.listdir(path_file)
# fullpaths = map(lambda name: os.path.join(path_file, name), dirfiles)
# dirs = []
# data = []
# for file in fullpaths:
#     if os.path.isdir(file): dirs.append(file)
#     os.getcwd()
# x = list(dirs)  #########   x is user Path find
# user = []  ########  All User List
# for i in x:
#     project_path = os.listdir(i)
#     users = i.split('\\')
#     user.append(users[5])
#     folder_project = map(lambda name: os.path.join(i, name), project_path)
#     fll = []
#     for profolder in folder_project:
#         if os.path.isdir(profolder): fll.append(profolder)
#         os.getcwd()
#     y1 = list(fll)
#     path_list_all = []  ########  Path_list_all contain All Genome (DNA, RNA, FFPC)
#     for j in y1:  #####  J is 240, 245 and 101, 102  print
#         prounder_path = os.listdir(j)
#         pro_folder = map(lambda name: os.path.join(j, name), prounder_path)
#         path = []
#         for f in pro_folder:
#             if os.path.isdir(f): path.append(f)
#             os.getcwd()
#         y2 = list(path)
#         for y in y2:
#             path_list_all.append(y)
#
#     fastqc_path_all = []  ###### FastQc all list
#     for plist in path_list_all:
#         fqc_path = os.listdir(plist)
#         fqc_folder = map(lambda name: os.path.join(plist, name), fqc_path)
#         fqc_list = []
#         for fq in fqc_folder:
#             if os.path.isdir(fq): fqc_list.append(fq)
#             os.getcwd()
#         y3 = list(fqc_list)
#         for x1 in y3:
#             fastqc_path_all.append(x1)
#     sq_path_all = []
#     for sr in fastqc_path_all:
#         s_sample = os.listdir(sr)
#         s_folder = map(lambda name: os.path.join(sr, name), s_sample)
#         s_list = []
#         for sq in s_folder:
#             if os.path.isdir(sq): s_list.append(sq)
#             os.getcwd()
#         y4 = list(s_list)
#         for x2 in y4:
#             sq_path_all.append(x2)
#     for s in sq_path_all:
#         pass


def upload_data(request):
    if request.user.is_authenticated:
        pro_file = os.path.join(BASE_DIR / 'media/project')
        projectfiles = os.listdir(pro_file)
        projectpaths = map(lambda name: os.path.join(pro_file, name), projectfiles)
        dirs = []
        for file in projectpaths:
            if os.path.isdir(file): dirs.append(file)
            os.getcwd()
        x = list(dirs)  #########   x is user Path find
        user = []  ########  All User List
        for i in x:
            project_path = os.listdir(i)
            users = i.split('\\')
            user.append(users[5])
            folder_project = map(lambda name: os.path.join(i, name), project_path)
            fll = []
            for profolder in folder_project:
                if os.path.isdir(profolder): fll.append(profolder.split('\\'))
                os.getcwd()
            for j in fll:
                project = j[5]
                patient = j[6]
                if ProjectTable.objects.filter(Q(Project=project) & Q(Patient=patient)).exists():
                    messages.success(request, 'New Data Not Updated All Data are Present')
                else:
                    st = ProjectTable(Project=project, Patient=patient)
                    st.save()
                    messages.success(request, 'New Dat Updated Congratulations!!!!!')

        return render(request, 'profile.html')


def patient_data(request):
    if request.user.is_authenticated:
        path_file = os.path.join(BASE_DIR / 'media/project')
        dirfiles = os.listdir(path_file)
        fullpaths = map(lambda name: os.path.join(path_file, name), dirfiles)
        dirs = []
        for file in fullpaths:
            if os.path.isdir(file): dirs.append(file)
            os.getcwd()
        x = list(dirs)  #########   x is user Path find
        user = []  ########  All User List
        for i in x:
            project_path = os.listdir(i)
            users = i.split('\\')
            user.append(users[5])
            folder_project = map(lambda name: os.path.join(i, name), project_path)
            fll = []
            for profolder in folder_project:
                if os.path.isdir(profolder): fll.append(profolder)
                os.getcwd()
            y1 = list(fll)
            path_list_all = []  ########  Path_list_all contain All Genome (DNA, RNA, FFPC)
            for j in y1:  #####  J is 240, 245 and 101, 102  print
                prounder_path = os.listdir(j)
                pro_folder = map(lambda name: os.path.join(j, name), prounder_path)
                path = []
                for f in pro_folder:
                    if os.path.isdir(f): path.append(f)
                    os.getcwd()
                y2 = list(path)
                for k in y2:
                    path_list_all.append(k)
            y3 = list(path_list_all)
            fastqc_path = []
            for k in y3:
                fqc_path = os.listdir(k)
                fqc_fol = map(lambda name: os.path.join(k, name), fqc_path)
                path1 = []
                for k1 in fqc_fol:
                    if os.path.isdir(k1): path1.append(k1)
                    os.getcwd()
                for s in path1:
                    fastqc_path.append(s)
            y4 = list(fastqc_path)
            for l in y4:
                fast_qc = os.listdir(l)
                fast_fol = map(lambda name: os.path.join(l, name), fast_qc)
                path2 = []
                for l1 in fast_fol:
                    if os.path.isdir(l1): path2.append(l1.split('\\'))
                    os.getcwd()
                for s1 in path2:
                    project = s1[5]
                    patient = s1[6]
                    sequence = s1[7]
                    fastqcfol = s1[8]
                    samplename = s1[9]
                    if Data1.objects.filter(
                            Q(Patient=patient) & Q(Sequence=sequence) & Q(Samplename=samplename)).exists():
                        messages.success(request, 'New Data Not be updated ')
                    else:
                        insert = Data1(Project=project, Patient=patient, Sequence=sequence, Fastqcfol=fastqcfol,
                                       Samplename=samplename)
                        insert.save()
                        messages.success(request, 'New Entery Upload Successfully !!!!')
        return render(request, 'profile.html')


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
                    messages.success(request, "Registration successful.")
                    return redirect('login')
                else:
                    messages.error(request, "Unsuccessful registration. Invalid information.")
                    form1 = LoginForm()
                    form2 = NewUserForm()
                    return render(request, 'login_regis.html', {'login_form': form1, 'register_form': form2})

            if request.POST.get('signin'):
                form = LoginForm(request, data=request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('home')
                    else:
                        messages.error(request, "Invalid username or password.")
                else:
                    messages.error(request, "Invalid username or password.")
                form = LoginForm()
                return render(request, 'login_regis.html', {'login_form': form})


class HomeView(View):
    def get(self, request, pt=None):
        if pt is None:
            print("Not Pt")
            prodata = Data1.objects.values('Project').distinct()
            return render(request, 'profile.html', {'prodata': prodata})

        if pt is not None:
            patient = Data1.objects.filter(Project=pt).values('Patient').distinct()
            ptd_dat = patient.values('Patient', 'Sequence', 'Samplename').distinct()
            newptd = patient.values('Sequence').distinct()
            prodata = Data1.objects.values('Project').distinct()
            return render(request, 'profile.html', {'prodata': prodata, 'patient': patient,
                                                    'sqt': ptd_dat, 'smp': newptd})


def show_data(request, data):
    pass
    return render(request, 'profile.html')

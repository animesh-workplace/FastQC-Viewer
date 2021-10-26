from django.db.models import Q, Count, Max
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from api.forms import LoginForm, NewUserForm, EditForm, FilterForm
from backend.settings import BASE_DIR, MEDIA_URL
from .models import Data1, Data2
from zipfile import ZipFile
import os
import glob
from django.views.decorators.csrf import csrf_exempt


# Main Code
@csrf_exempt
def data_store(request):
    if request.user.is_authenticated:
        path_file = os.path.join(BASE_DIR / 'media/Project')
        dirfiles = os.listdir(path_file)
        fullpaths = map(lambda name: os.path.join(path_file, name), dirfiles)
        dirs = []
        for file in fullpaths:
            if os.path.isdir(file): dirs.append(file)
            os.getcwd()
        x = list(dirs)  #########   x is user Path find
        for i in x:
            project_path = os.listdir(i)
            folder_project = map(lambda name: os.path.join(i, name), project_path)
            fll = []
            for profolder in folder_project:
                if os.path.isdir(profolder): fll.append(profolder)
                os.getcwd()
            y1 = list(fll)
            path_list_all = []
            for j in y1:
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
            last_path = []
            for l in y4:
                fast_qc = os.listdir(l)
                fast_fol = map(lambda name: os.path.join(l, name), fast_qc)
                path2 = []
                for l1 in fast_fol:
                    if os.path.isdir(l1): path2.append(l1)
                    os.getcwd()
                for s1 in path2:
                    last_path.append(s1)
            y5 = list(last_path)
            sample_path = []
            for r in y5:
                sam = os.listdir(r)
                samp_fol = map(lambda name: os.path.join(r, name), sam)
                for r1 in samp_fol:
                    if os.path.isdir(r1): sample_path.append(r1)
                    os.getcwd()
            y6 = list(sample_path)
            for o in y6:
                os.chdir(o)
                text_file = glob.glob('*.txt')
                image_path = o.split('/')
                new_split = image_path[12].split('_')
                image_path.append(new_split[0])
                image_path.append(new_split[1])
                image_path.append(new_split[2])
                image_path.append(new_split[3])
                image_path.append(new_split[4])
                image_path.append(new_split[5])
                with open(text_file[0], 'r') as f1, open(text_file[1], 'r') as f2:
                    read_file = f2.read().split()
                    fastqc_file = f1.read().split()
                image_path.append(read_file[0])
                image_path.append(read_file[4])
                image_path.append(read_file[10])
                image_path.append(read_file[16])
                image_path.append(read_file[22])
                image_path.append(read_file[28])
                image_path.append(read_file[34])
                image_path.append(read_file[40])
                image_path.append(read_file[45])
                image_path.append(read_file[50])
                image_path.append(read_file[54])
                image_path.append(fastqc_file[21])
                image_path.append(fastqc_file[30])
                image_path.append(fastqc_file[32])
                main_path = image_path.index('media')
                new_path = image_path[main_path:]
                sequence = new_path[4]
                fastqc = new_path[5]
                samplename = new_path[6]
                pathname = new_path[7]
                trusqc = new_path[9]
                flowcell = new_path[10]
                lane = new_path[11]
                row = new_path[12]
                bs = new_path[14]
                pbsq = new_path[15]
                ptsq = new_path[16]
                psqs = new_path[17]
                pbsc = new_path[18]
                psgc = new_path[19]
                pbnc = new_path[20]
                sld = new_path[21]
                sdl = new_path[22]
                oss = new_path[23]
                ac = new_path[24]
                tsqc = new_path[25]
                sqclth = new_path[26]
                gc = new_path[27]
                if Data2.objects.filter(Q(Sequence=sequence) & Q(Sample_name=samplename) &
                                        Q(Lane=lane) & Q(Row=row)).exists():
                    pass
                else:
                    st = Data2(Sequence=sequence, FastQc=fastqc, Sample_name=samplename, Path_name=pathname,
                               Tru_Sequence=trusqc, Flowcell=flowcell, Lane=lane, Row=row, BS=bs, PBSQ=pbsq,
                               PTSQ=ptsq, PSQS=psqs, PBSC=pbsc, PSGC=psgc, PBNC=pbnc, SLD=sld, SDL=sdl, OS=oss,
                               AC=ac, Total_Sequence=tsqc, Sequence_length=sqclth, GC=gc)
                    st.save()
        messages.success(request, "Data Uploaded !!!!!")
        return render(request, 'profile.html')


@csrf_exempt
def patient_data(request):
    if request.user.is_authenticated:
        path_file = os.path.join(BASE_DIR / 'media/Project')
        dirfiles = os.listdir(path_file)
        fullpaths = map(lambda name: os.path.join(path_file, name), dirfiles)
        dirs = []
        for file in fullpaths:
            if os.path.isdir(file): dirs.append(file)
            os.getcwd()
        x = list(dirs)
        for i in x:
            project_path = os.listdir(i)
            folder_project = map(lambda name: os.path.join(i, name), project_path)
            fll = []
            for profolder in folder_project:
                if os.path.isdir(profolder): fll.append(profolder)
                os.getcwd()
            y1 = list(fll)
            path_list_all = []
            for j in y1:
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
                    if os.path.isdir(l1): path2.append(l1.split('/'))
                    os.getcwd()
                for s1 in path2:
                    main_path = s1.index('media')
                    new_path = s1[main_path:]
                    project = new_path[2]
                    patient = new_path[3]
                    sequence = new_path[4]
                    fastqcfol = new_path[5]
                    samplename = new_path[6]
                    sample = new_path[6][4:]
                    if Data1.objects.filter(
                            Q(Patient=patient) & Q(Sequence=sequence) & Q(Samplename=samplename)).exists():
                        pass
                    else:
                        insert = Data1(Project=project, Patient=patient, Sequence=sequence, Fastqcfol=fastqcfol,
                                       Samplename=samplename, Sample=sample)
                        insert.save()
        messages.success(request, "Work Done !!!!!!!")
        return render(request, 'profile.html')


class CustomerRegView(View):
    @csrf_exempt
    def get(self, request):
        form1 = LoginForm()
        form2 = NewUserForm()
        return render(request, 'login_regis.html', {'login_form': form1, 'register_form': form2})

    @csrf_exempt
    def post(self, request):
        if request.method == "POST":
            if request.POST.get('signup'):
                form = NewUserForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    messages.success(request, "Registration successful. !!!!1")
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
                        messages.success(request, "Welcome you are loggedin.")
                        return redirect('home')
                    else:
                        messages.error(request, "Invalid username or password.")
                else:
                    messages.error(request, "Invalid username or password.")
                form1 = LoginForm()
                form2 = NewUserForm()
                return render(request, 'login_regis.html', {'login_form': form1, 'register_form': form2})


class HomeView(View):
    def get(self, request, pt=None):
        if pt is None:
            prodata = Data1.objects.values('Project').distinct()
            return render(request, 'profile.html', {'prodata': prodata})

        if pt is not None:
            patient = Data1.objects.filter(Project=pt).values('Patient').distinct()
            ptd_dat = patient.values('Project', 'Patient', 'Sequence', 'Samplename', 'Sample').distinct()
            newptd = patient.values('Sequence').distinct()  # Sequence Send
            prodata = Data1.objects.values('Project').distinct()

            return render(request, 'profile.html', {'prodata': prodata, 'patient': patient,
                                                    'sqt': ptd_dat, 'smp': newptd, 'sqc': pt})


@csrf_exempt
def show_data(request, dt=None, pt=None, data=None, data1=None):
    if dt is None and data is None and data1 is None:
        prodata = Data1.objects.values('Project').distinct()
        return render(request, {'prodata': prodata})
    if dt is not None and data is not None and data1 is not None:
        sample = Data2.objects.filter(Q(Sequence=data) & Q(Sample_name=data1))
        prodata = Data1.objects.values('Project').distinct()
        form = EditForm()
        return render(request, 'profile.html', {'prodata': prodata, 'sample': sample, 'pro': dt, 'pt': pt,
                                                'sqc': data, 'spp': data1, 'editform': form})


def delete(request, id):
    if request.method == 'GET':
        dl = Data2.objects.get(pk=id)
        dl.delete()
        messages.success(request, "Data Deleted Successfully !!!!!!!")
        return HttpResponseRedirect('/')

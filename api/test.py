from zipfile import ZipFile
from django.conf import settings
from django.conf.urls.static import static
from os import listdir
from os.path import isfile, join
from collections import Counter

from zipfile import ZipFile
import os
import glob
import time
import re
from os import listdir
from os.path import isfile, join

from backend.settings import BASE_DIR, MEDIA_URL


path_file = os.path.join(BASE_DIR / 'media/Project')
dirfiles = os.listdir(path_file)
fullpaths = map(lambda name: os.path.join(path_file, name), dirfiles)
dirs = []
data = []
folder = []
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
    path_list_all = [] ########  Path_list_all contain All Genome (DNA, RNA, FFPC)
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
        md = image_path.index('media')
        new_root = image_path[md:]
        new_split = new_root[7].split('_')
        new_root.append(new_split[0])
        new_root.append(new_split[1])
        new_root.append(new_split[2])
        new_root.append(new_split[3])
        new_root.append(new_split[4])
        new_root.append(new_split[5])
        with open(text_file[0], 'r') as f1, open(text_file[1], 'r') as f2:
            read_file = f2.read().split()
            fastqc_file = f1.read().split()
        new_root.append(read_file[0])
        new_root.append(read_file[4])
        new_root.append(read_file[10])
        new_root.append(read_file[16])
        new_root.append(read_file[22])
        new_root.append(read_file[28])
        new_root.append(read_file[34])
        new_root.append(read_file[40])
        new_root.append(read_file[45])
        new_root.append(read_file[50])
        new_root.append(read_file[54])
        new_root.append(fastqc_file[21])
        new_root.append(fastqc_file[30])
        new_root.append(fastqc_file[32])
        sequence = new_root[4]
        fastqc = new_root[5]
        samplename = new_root[6]
        pathname = new_root[7]
        trusqc = new_root[9]
        flowcell = new_root[10]
        lane = new_root[11]
        row = new_root[12]
        bs = new_root[14]
        pbsq = new_root[15]
        ptsq = new_root[16]
        psqs = new_root[17]
        pbsc = new_root[18]
        psgc = new_root[19]
        pbnc = new_root[20]
        sld = new_root[21]
        sdl = new_root[22]
        oss = new_root[23]
        ac = new_root[24]
        tsqc = new_root[25]
        sqclth = new_root[26]
        gc = new_root[27]
        print(new_root)


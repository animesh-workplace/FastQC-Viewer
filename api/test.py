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


path_file = os.path.join(BASE_DIR / 'media/project')
dirfiles = os.listdir(path_file)
fullpaths = map(lambda name: os.path.join(path_file, name), dirfiles)
dirs = []
data = []
folder = []
for file in fullpaths:
    if os.path.isdir(file): dirs.append(file)
    os.getcwd()
x = list(dirs)  #########   x is user Path find
user = []   ########  All User List
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
    path_list_all = [] ########  Path_list_all contain All Genome (DNA, RNA, FFPC)
    for j in y1:   #####  J is 240, 245 and 101, 102  print
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
        image_path = o.split('\\')
        new_split = image_path[10].split('_')
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
        print(image_path[7:])

#     for o in y:
#         os.chdir(o)
#         text_file = glob.glob('*.txt')
#         image_path = o.split('\\')
#         new_split = image_path[8].split('_')
#         name = ['a', 'b', 'c', 'd', 'e', 'Project_name', 'Sub_folder', 'fastqc', 'Path', 'Date', 'Sample_name',
#                 'TrueSq', 'Flowcell', 'Lane', 'Row', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
#                 '11', 'Total_Sequence', 'Lenth', '%GC', 'im1', 'im2', 'im3', 'im4', 'im5',
#                 'im6', 'im7', 'im8', 'img9']
#         path_time = os.path.getatime(o)
#         c_ti = time.ctime(path_time)
#         t_obj = time.strptime(c_ti)
#         T_stamp = time.strftime("%d-%m-%Y %H:%M:%S", t_obj)
#         image_path.append(T_stamp[0:10])
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
#         imagefolder.append(o)
#     img_list = []
#     for d in imagefolder:
#         imagefol_path = os.listdir(d)
#         imgfolder_list = map(lambda name: os.path.join(d, name), imagefol_path)
#         fll = []
#         for imgfolder in imgfolder_list:
#             if os.path.isdir(imgfolder): fll.append(imgfolder)
#             os.getcwd()
#         y1 = list(fll)
#         img_list.append(y1[1])
#     for img in img_list:
#         for root, dirs, files, in os.walk(img):
#             image_path.append(files[0])
#             image_path.append(files[1])
#             image_path.append(files[2])
#             image_path.append(files[3])
#             image_path.append(files[4])
#             image_path.append(files[5])
#             image_path.append(files[6])
#             image_path.append(files[7])
#             image_path.append(files[8])
#
#         dictfile = zip(name, image_path)
#         newdict = dict(dictfile)
#         data.append(newdict)
#
# print(type(data[0].values()))
# # file_name1 = "/home/nibmg/Desktop/folderpro/backend/api/zipfiles/2240111_TruseqNano_HYGWFDSXY_L1_R2_fastqc.zip"
# # file_name2 = "/home/nibmg/Desktop/folderpro/backend/api/zipfiles/2240111_TruseqNano_HYGWFDSXY_L1_R1_fastqc.zip"
# #
# #
# # counts = Counter()
# # for c_dir, dirnames, filenames in os.walk('.'):
# #     for filename in filenames:
# #         before_ext, extension = os.path.splitext(filename)
# #         counts[extension] += 1
# # with ZipFile(file_name1, 'r') as zip:
# #     zip.printdir()
# #     print(zip.infolist())
# #
# #     # extracting all the files
# #     print('Extracting all the files now...')
# #     zip.extractall('zipfiles')
# #     print('Done!')
# #     print(dir(zip))
# # for extension, count in counts.items():
# #     ext = f"{extension:6}{count}"
# #     print("The Extension Name", type(ext))
# # Path where we have to count files and directories
#
# #              For Zipfolder subdirectiory
# import forloop as forloop
#
# HOME_FOLDER = 'E:/Python Program/FolderPro/api/static/zipfiles'
# dirfiles = os.listdir(HOME_FOLDER)
# fullpaths = map(lambda name: os.path.join(HOME_FOLDER, name), dirfiles)
# dirs = []
# files = []
# data = []
# text_list = []
# for file in fullpaths:
#     if os.path.isdir(file): dirs.append(file)
#     if os.path.isfile(file): files.append(file)
# # print("Fullpath Files list", dirs)
#
# x = list(dirs)
# # for path, dirs, f in os.walk(HOME_FOLDER):
# #     # print(path)
# #     print("Files", f)
#
# for i in x:
#     sep = i.split('_')
#     os.chdir(i)
#     text_file = glob.glob('*.txt')
#     image_path = i.split('\\')
#     new_split = image_path[1].split('_')
#     name = ['Sample_name', 'True_Sequence', 'Flowcell', 'Lane', 'Rack', 'Fastqc', 'Date', 'Path',
#             '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 'Total_Sequence', 'Lenth', '%GC']
#     path_time = os.path.getctime(i)
#     c_ti = time.ctime(path_time)
#     new_split.append(c_ti)
#     new_split.append(image_path[1])
#     print(new_split)
#     with open(text_file[0], 'r') as f1, open(text_file[1], 'r') as f2:
#         read_file = f2.read().split()
#         fastqc_file = f1.read().split()
#     new_split.append(read_file[0])
#     new_split.append(read_file[4])
#     new_split.append(read_file[10])
#     new_split.append(read_file[16])
#     new_split.append(read_file[22])
#     new_split.append(read_file[28])
#     new_split.append(read_file[34])
#     new_split.append(read_file[40])
#     new_split.append(read_file[45])
#     new_split.append(read_file[50])
#     new_split.append(read_file[54])
#     new_split.append(fastqc_file[21])
#     new_split.append(fastqc_file[30])
#     new_split.append(fastqc_file[32])
#     dictfile = zip(name, new_split)
#     newdict = dict(dictfile)
#     data.append(newdict)
# print(data)
#         # for f in text_file:
#     #     infile = open(f, 'r')
#     #     read_f = infile.read()
#     #     print(read_f)
#     # for f in text_file:
#     #     outfile = open(f, 'r')
#     #     read_file = outfile.read().split()
#     #     outfile.close()
#     #     # print(read_file)
#     # sep.append(read_file[0])
#     # sep.append(read_file[4])
#     # sep.append(read_file[10])
#     # sep.append(read_file[16])
#     # sep.append(read_file[22])
#     # sep.append(read_file[28])
#     # sep.append(read_file[34])
#     # sep.append(read_file[40])
#     # sep.append(read_file[45])
#     # sep.append(read_file[50])
#     # sep.append(read_file[54])
#     # dictfile = zip(name, sep)
#     # newdict = dict(dictfile)
#     # data.append(newdict)
#
#
# # print(i)
# # print(res[4][0] == 'R2')
# # print(res[0][1] == '2240131')
# #
# # files_list = [f for f in listdir('E:/Python Program/FolderPro/api/static/zipfiles')
# #               if isfile(join('E:/Python Program/FolderPro/api/static/zipfiles', f))]
# # print("Before For Loop", files_list)
# # noOfFiles = 0
# # noOfDir = 0
# #
# # for base, dirs, files in os.walk(HOME_FOLDER):
# # print('Looking in : ', base)
# # for directories in dirs:
# #     noOfDir += 1
# # for Files in files:
# #     noOfFiles += 1
# # print(dirs)
# #
# # print(type(files))
# # print('Number of files', noOfFiles)
# # print('Number of Directories', noOfDir)
# # print('Total:', (noOfDir + noOfFiles))

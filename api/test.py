from zipfile import ZipFile
import os
import time
from os import listdir
from os.path import isfile, join
from collections import Counter
import re

# file_name1 = "/home/nibmg/Desktop/folderpro/backend/api/zipfiles/2240111_TruseqNano_HYGWFDSXY_L1_R2_fastqc.zip"
# file_name2 = "/home/nibmg/Desktop/folderpro/backend/api/zipfiles/2240111_TruseqNano_HYGWFDSXY_L1_R1_fastqc.zip"
#
#
# counts = Counter()
# for c_dir, dirnames, filenames in os.walk('.'):
#     for filename in filenames:
#         before_ext, extension = os.path.splitext(filename)
#         counts[extension] += 1
# with ZipFile(file_name1, 'r') as zip:
#     zip.printdir()
#     print(zip.infolist())
#
#     # extracting all the files
#     print('Extracting all the files now...')
#     zip.extractall('zipfiles')
#     print('Done!')
#     print(dir(zip))
# for extension, count in counts.items():
#     ext = f"{extension:6}{count}"
#     print("The Extension Name", type(ext))
# Path where we have to count files and directories

#              For Zipfolder subdirectiory
HOME_FOLDER = 'E:/Python Program/FolderPro/api/static/zipfiles'
dirfiles = os.listdir(HOME_FOLDER)
fullpaths = map(lambda name: os.path.join(HOME_FOLDER, name), dirfiles)
dirs = []
files = []
data = []
for file in fullpaths:
    if os.path.isdir(file): dirs.append(file)
    if os.path.isfile(file): files.append(file)
print("Fullpath Files list", dirs)
x = list(dirs)
for i in x:
    sep = i.split('_')
    image_path = i.split('\\')
    name = ['Sample_name', 'True_Sequence', 'Flowcell', 'Lane', 'Rack', 'Fastqc', 'Date', 'Path']
    path_time = os.path.getctime(i)
    c_ti = time.ctime(path_time)
    sep.append(c_ti)
    sep.append(image_path[1])
    dictfile = zip(name, sep)
    newdict = dict(dictfile)
    data.append(newdict)
    print(sep)
print(data)




# print(i)
# print(res[4][0] == 'R2')
# print(res[0][1] == '2240131')
#
# files_list = [f for f in listdir('E:/Python Program/FolderPro/api/static/zipfiles')
#               if isfile(join('E:/Python Program/FolderPro/api/static/zipfiles', f))]
#  print("Before For Loop", files_list)
# for root, dirs, files in os.walk(HOME_FOLDER):
#     for x in dirs:
#         print(x)
# noOfFiles = 0
# noOfDir = 0
#
# for base, dirs, files in os.walk(HOME_FOLDER):
    # print('Looking in : ', base)
    # for directories in dirs:
    #     noOfDir += 1
    # for Files in files:
    #     noOfFiles += 1
    # print(dirs)
#
# print(type(files))
# print('Number of files', noOfFiles)
# print('Number of Directories', noOfDir)
# print('Total:', (noOfDir + noOfFiles))

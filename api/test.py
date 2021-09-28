from zipfile import ZipFile
import os
import time
import glob
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
import forloop as forloop

HOME_FOLDER = 'E:/Python Program/FolderPro/api/static/zipfiles'
dirfiles = os.listdir(HOME_FOLDER)
fullpaths = map(lambda name: os.path.join(HOME_FOLDER, name), dirfiles)
dirs = []
files = []
data = []
text_list = []
for file in fullpaths:
    if os.path.isdir(file): dirs.append(file)
    if os.path.isfile(file): files.append(file)
print("Fullpath Files list", dirs)

x = list(dirs)
# for path, dirs, f in os.walk(HOME_FOLDER):
#     # print(path)
#     print("Files", f)

for i in x:
    sep = i.split('_')
    os.chdir(i)
    text_file = glob.glob('*.txt')

    image_path = i.split('\\')
    name = ['Sample_name', 'True_Sequence', 'Flowcell', 'Lane', 'Rack', 'Fastqc', 'Date', 'Path',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    path_time = os.path.getctime(i)
    c_ti = time.ctime(path_time)
    sep.append(c_ti)
    sep.append(image_path[1])
    with open(text_file[0], 'r') as f1, open(text_file[1], 'r') as f2:
        file1 = f1.read()
        file2 = f2.read()
    print("FastQc Text File", file1)
    print("Summury Text File", file2)
    # for f in text_file:
    #     infile = open(f, 'r')
    #     read_f = infile.read()
    #     print(read_f)
    # for f in text_file:
    #     outfile = open(f, 'r')
    #     read_file = outfile.read().split()
    #     outfile.close()
    #     # print(read_file)
    # sep.append(read_file[0])
    # sep.append(read_file[4])
    # sep.append(read_file[10])
    # sep.append(read_file[16])
    # sep.append(read_file[22])
    # sep.append(read_file[28])
    # sep.append(read_file[34])
    # sep.append(read_file[40])
    # sep.append(read_file[45])
    # sep.append(read_file[50])
    # sep.append(read_file[54])
    # dictfile = zip(name, sep)
    # newdict = dict(dictfile)
    # data.append(newdict)


# print(i)
# print(res[4][0] == 'R2')
# print(res[0][1] == '2240131')
#
# files_list = [f for f in listdir('E:/Python Program/FolderPro/api/static/zipfiles')
#               if isfile(join('E:/Python Program/FolderPro/api/static/zipfiles', f))]
# print("Before For Loop", files_list)
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

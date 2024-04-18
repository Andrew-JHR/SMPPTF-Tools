# Check if a PTF exists by reading the resulting files of an SMPE LIST SYSMOD
# if that PTF exists then remove it
# Author : Andrew Jan
# Date   : 2022/10/28
# Update : 2023/02/17

import os
import shutil

dir = r'D:\logs\U02465002_B7908793_PROD\SMPPTFIN\\'

files = []

for file in os.listdir(dir):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir, file)):
        if 'pax.Z' in file:
           continue
        elif 'SMPPTFIN' in file:
           continue
        else:   
           files.append(file)

output = open(dir + 'SMPPTFIN1', "wb")

for i in range(len(files)):
    # if os.path.exists(os.path.join(ipath, files[i])):
    shutil.copyfileobj(open(dir + files[i], "rb"), output)

output.close()
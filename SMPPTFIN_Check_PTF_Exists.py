# Check to see if a PTF exists by reading the resulting files of an SMPE LIST SYSMOD
# if that PTF exists then remove it
# Use the following JCL statements to get a list of all PTFs applied;
# Save all the running result to a sequential file or PDS member (FBA 134)
# Download (Text-Mode) the file as 'SYSMOD....txt'
# 
# //ANDREWJL  JOB  CLASS=A,NOTIFY=&SYSUID,MSGCLASS=X
# //LIST      EXEC PGM=GIMSMP,REGION=0M
# //SMPCSI    DD  DSN=SMPE.GLOBAL.CSI,DISP=SHR
# //SMPCNTL   DD  *
#    SET    BDY(MVST100).
#    LIST SYSMOD.
# /*
# //
#
# Those already applied PTFs will be deleted from the folder
#
# Author : Andrew Jan
# Date   : 2023/09/19

import os

ipath =r'D:\logs\U02465002_B7908793_PROD\SMPPTFIN\\'
rpath = r'D:\logs\SYSMOD 20230919.txt'

sysmods = list()
fp = open(rpath)
while True:
   line = fp.readline()
   if not line:    #eof
      break
   if line[11:29] == 'TYPE            = ':
      sysmods.append(line[1:8]) 
fp.close()

#for i in range(len(sysmods)):
#    print(sysmods[i])

files = []

for file in os.listdir(ipath):
    # check if current path is a file
    if os.path.isfile(os.path.join(ipath, file)):
        files.append(file)

for i in range(len(files)):
    # if os.path.exists(os.path.join(ipath, files[i])):
    if files[i] in sysmods:  
       os.remove(os.path.join(ipath, files[i]))
       print(files[i] + " deleted! ")

exit()
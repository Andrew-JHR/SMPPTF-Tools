import shutil

dir = r'D:\logs\U02465002_B7908793_PROD\SMPPTFIN'
file = '2023285230327712402'
num = 9

dir = dir + '\\'

output = open(dir + file + '.pax.Z', "wb")

for i in range(1,num+1):
    shutil.copyfileobj(open(dir + file + '.' + str(i) + 'of' + str(num), "rb"), output)

output.close()
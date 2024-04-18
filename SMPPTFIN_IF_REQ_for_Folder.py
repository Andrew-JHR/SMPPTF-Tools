# find out conditional required PTFs
# Author: Andrew Jan
# Date of Creation: 2023/02/07
# Date of Update  : 2023/02/07



dir = r'D:\logs\U02465002_B7908793_PROD\SMPPTFIN\\'

record_len = 80

LP01 =  [
         'EDU1H01','EER3500','EMI2220','ETI1106','FDU1H07','FDU1H08','HAL47C0',
         'HBB77C0','HBD6602','HCM1H10','HCPT440','HCRY740','HCR77D0','HCS77C0',
         'HDZ224N','HDZ2240','HFST101','HFX1112','HGD3200','HGD3201','HHAP90P',
         'HIF7S02','HIO1104','HIP6240','HIT7750','HJE77C0','HJVA800','HJVB800',
         'HKCZ120','HKY77C0','HLB77C0','HLE77C0','HMP1K00','HMQ4160','HOS2240',
         'HOT77C0','HPG77C0','HPM77C0','HPV77B0','HQX77C0','HRF77C0','HRM77C0',
         'EDU1H01','EER3500','EMI2220','ETI1106','FDU1H07','FDU1H08','HAL47C0',
         'HBB77C0','HBD6602','HCM1H10','HCPT440','HCRY740','HCR77D0','HCS77C0',
         'HDZ224N','HDZ2240','HFST101','HFX1112','HGD3200','HGD3201','HHAP90P',
         'HIF7S02','HIO1104','HIP6240','HIT7750','HJE77C0','HJVA800','HJVB800',
         'HKCZ120','HKY77C0','HLB77C0','HLE77C0','HMP1K00','HMQ4160','HOS2240',
         'HOT77C0','HPG77C0','HPM77C0','HPV77B0','HQX77C0','HRF77C0','HRM77C0',
         'HRO7740','HRSL440','HSD7780','HSMA24A','HSMA24E','HSMA240','HSMA241',
         'HSMA242','HSMA243','HSMA244','HSMA245','HSMA246','HSMA247','HSM1P00',
         'HSWF100','HSWK440','HTE77C0','HTV77C0','HUN77B0','HVT6240','HWJ9143',
         'HWLPEM0','HZDC7C0','HZFS440','H0GB310','H24P111','JBD6201','JBD6202',
         'JCPT441','JCRY741','JGD3219','JIP624K','JIP624X','JMQ416A','JRSL441',
         'JSWK441','JTE77CE', 
        ]  
LP0E =  [
         'EDU1H01','EER3500','EMI2220','ETI1106','FDU1H07','FDU1H08','HADB630',
         'HAL47C0','HBB77C0','HBD6602','HCM1H10','HCPT440','HCRY740','HCR77D0',
         'HCS77C0','HDZ224N','HDZ2240','HFNT130','HFST101','HFX1112','HGD3200',
         'HGD3201','HHAP90P','HIF7S02','HIO1104','HIP6240','HIT7750','HJE77C0',
         'HJVA800','HJVB800','HKCZ120','HKDS630','HKLV630','HKY77C0','HLB77C0',
         'HLE77C0','HMOS705','HMP1K00','HMQ4160','HMS9100','HNET7C0','HOPI7C0',
         'EDU1H01','EER3500','EMI2220','ETI1106','FDU1H07','FDU1H08','HADB630',
         'HAL47C0','HBB77C0','HBD6602','HCM1H10','HCPT440','HCRY740','HCR77D0',
         'HCS77C0','HDZ224N','HDZ2240','HFNT130','HFST101','HFX1112','HGD3200',
         'HGD3201','HHAP90P','HIF7S02','HIO1104','HIP6240','HIT7750','HJE77C0',
         'HJVA800','HJVB800','HKCZ120','HKDS630','HKLV630','HKY77C0','HLB77C0',
         'HLE77C0','HMOS705','HMP1K00','HMQ4160','HMS9100','HNET7C0','HOPI7C0',
         'HOS2240','HOT77C0','HPG77C0','HPM77C0','HPV77B0','HQX77C0','HRF77C0',
         'HRM77C0','HRO7740','HRSL440','HSD7780','HSMA24A','HSMA24E','HSMA240',
         'HSMA241','HSMA242','HSMA243','HSMA244','HSMA245','HSMA246','HSMA247',
         'HSM1P00','HSWF100','HSWK440','HTE77C0','HTV77C0','HUN77B0','HVT6240',
         'HWJ9143','HWLPEM0','HZDC7C0','HZFS440','H0GB310','H24P111','JADB63H',
         'JADB631','JBD6201','JBD6202','JCPT441','JCRY741','JGD3219','JIP624K',
         'JIP624X','JMQ416A','JMS9101','JMS9102','JMS9103','JMS9104','JMS9105',
         'JMS9106','JMS9108','JRSL441','JSWK441','JTE77CE',       
        ]


fmid = LP0E

e = dict()
for i in range(0,256):
   e[i] = ' '

#e[0x4A] = '¢' 
e[0x4B] = '.'  
e[0x4C] = '<'  
e[0x4D] = '('  
e[0x4E] = '+'  
e[0x4F] = '|'  
e[0x50] = '&'  

e[0x5A] = '!'  
e[0x5B] = '$'  
e[0x5C] = '*'  
e[0x5D] = ')'  
e[0x5E] = ';'  
#e[0x5F] = '¬' 
e[0x60] = '-'  
e[0x61] = '/'  

e[0x6A] = '|'
e[0x6B] = ','
e[0x6C] = '%'
e[0x6D] = '_'
e[0x6E] = '>'
e[0x6F] = '?'

e[0x7A] = ':'
e[0x7B] = '#'
e[0x7C] = '@'
e[0x7D] = "'"
e[0x7E] = '='
e[0x7F] = '"'

e[0x81] = 'a'
e[0x82] = 'b'
e[0x83] = 'c'
e[0x84] = 'd'
e[0x85] = 'e'
e[0x86] = 'f'
e[0x87] = 'g'
e[0x88] = 'h'
e[0x89] = 'i'

e[0x91] = 'j'
e[0x92] = 'k'
e[0x93] = 'l'
e[0x94] = 'm'
e[0x95] = 'n'
e[0x96] = 'o'
e[0x97] = 'p'
e[0x98] = 'q'
e[0x99] = 'r'

e[0xA1] = '~'
e[0xA2] = 's'
e[0xA3] = 't'
e[0xA4] = 'u'
e[0xA5] = 'v'
e[0xA6] = 'w'
e[0xA7] = 'x'
e[0xA8] = 'y'
e[0xA9] = 'z'

e[0xC0] = '{'
e[0xC1] = 'A'
e[0xC2] = 'B'
e[0xC3] = 'C'
e[0xC4] = 'D'
e[0xC5] = 'E'
e[0xC6] = 'F'
e[0xC7] = 'G'
e[0xC8] = 'H'
e[0xC9] = 'I'

e[0xD0] = '}'
e[0xD1] = 'J'
e[0xD2] = 'K'
e[0xD3] = 'L'
e[0xD4] = 'M'
e[0xD5] = 'N'
e[0xD6] = 'O'
e[0xD7] = 'P'
e[0xD8] = 'Q'
e[0xD9] = 'R'

e[0xE0] = '\\'
 
e[0xE2] = 'S'
e[0xE3] = 'T'
e[0xE4] = 'U'
e[0xE5] = 'V'
e[0xE6] = 'W'
e[0xE7] = 'X'
e[0xE8] = 'Y'
e[0xE9] = 'Z'

e[0xF0] = '0'
e[0xF1] = '1'
e[0xF2] = '2'
e[0xF3] = '3'
e[0xF4] = '4'
e[0xF5] = '5'
e[0xF6] = '6'
e[0xF7] = '7'
e[0xF8] = '8'
e[0xF9] = '9'
e[0xFA] = '|'

keyw1 = b'NN@\xd7\xe3\xc6@M'   # '++ PTF (' in EBCDIC 
keyw2 = b'NN\xc9\xc6@'         # '++IF ' in EBCDIC 
keyw3 = b'NN@\xc9\xc6@'        # '++ IF ' in EBCDIC

import os

files = []

for file in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, file)):
       files.append(file)

for file in files:
    if file == 'SMPPTFIN':
       continue
    print('file: ' + file)
    ipath =  dir + file
    ifile = open(ipath,'rb')
    while True:
        bytes = ifile.read(record_len)
        if not bytes:    #eof
           break
        elif bytes[:8] == keyw1:
           ptfb = bytes[8:15]
           ptf = '' 
           for i in range(7):
              ptf = ptf + e[ptfb[i]]
           print(ptf)
        elif bytes[:5] == keyw2:
           req = ''
           for i in range(record_len):
              req = req + e[bytes[i]]
           if req[10:17] in fmid:    
              print(req)     
        elif bytes[:6] == keyw3:
           req = ''
           for i in range(record_len):
              req = req + e[bytes[i]]
           if req[11:18] in fmid:    
              print(req)           
    ifile.close()

exit()
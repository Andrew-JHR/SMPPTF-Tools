# Show the content of SMPPTFIN & SMPHOLD
# Author: Andrew Jan
# Date of Creation: 2022/10/23
# Date of Update  : 2022/10/23

record_len = 80

folder = r'D:\logs\U02465002_B7908793_PROD\SMPPTFIN\\'
ipath =  folder + 'SMPPTFIN'

ifile = open(ipath,'rb')

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

assigns = list() 
keyw = b'NN@\xd7\xe3\xc6@M'   # '++ PTF (' in EBCDIC 

while True:
    text  = ''
    bytes = ifile.read(record_len)
    for j in range(record_len):
       text  = text  + e[bytes[j]]
    if keyw in bytes:
       break 
    assigns.append(bytes)  
    print(text)

ptf = ''

while True:
    #if bytes[:8] == keyw:
    if keyw in bytes:
       if ptf != '': 
          ofile.close() 
       ptfb = bytes[8:15]
       ptf = '' 
       for i in range(7):
           ptf = ptf + e[ptfb[i]]
       print(ptf)
       ofile = open(folder + ptf, 'wb')
       for i in range(len(assigns)):
          if ptfb in assigns[i]:
             ofile.write(assigns[i])          
    
    ofile.write(bytes)
      
    bytes = ifile.read(record_len)
    if not bytes:    #eof
       break
    
   
ifile.close()
ofile.close() 


exit()
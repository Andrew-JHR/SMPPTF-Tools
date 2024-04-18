# Show the content of SMPPTFIN & SMPHOLD
# Author: Andrew Jan
# Date of Creation: 2022/10/07
# Date of Update  : 2022/10/07

record_len = 80

ipath = r'D:\logs\U02414610_B7697109_PROD\SMPPTFIN\SMPPTFIN1'
opath =  ipath + '.txt'

ofile = open(opath,'w')
ifile = open(ipath,'rb')

d = dict()
for i in range(0,256):
   d[i] = ' '

#d[0x4A] = '¢' 
d[0x4B] = '.'  
d[0x4C] = '<'  
d[0x4D] = '('  
d[0x4E] = '+'  
d[0x4F] = '|'  
d[0x50] = '&'  

d[0x5A] = '!'  
d[0x5B] = '$'  
d[0x5C] = '*'  
d[0x5D] = ')'  
d[0x5E] = ';'  
#d[0x5F] = '¬' 
d[0x60] = '-'  
d[0x61] = '/'  

d[0x6A] = '|'
d[0x6B] = ','
d[0x6C] = '%'
d[0x6D] = '_'
d[0x6E] = '>'
d[0x6F] = '?'

d[0x7A] = ':'
d[0x7B] = '#'
d[0x7C] = '@'
d[0x7D] = "'"
d[0x7E] = '='
d[0x7F] = '"'

d[0x81] = 'a'
d[0x82] = 'b'
d[0x83] = 'c'
d[0x84] = 'd'
d[0x85] = 'e'
d[0x86] = 'f'
d[0x87] = 'g'
d[0x88] = 'h'
d[0x89] = 'i'

d[0x91] = 'j'
d[0x92] = 'k'
d[0x93] = 'l'
d[0x94] = 'm'
d[0x95] = 'n'
d[0x96] = 'o'
d[0x97] = 'p'
d[0x98] = 'q'
d[0x99] = 'r'

d[0xA1] = '~'
d[0xA2] = 's'
d[0xA3] = 't'
d[0xA4] = 'u'
d[0xA5] = 'v'
d[0xA6] = 'w'
d[0xA7] = 'x'
d[0xA8] = 'y'
d[0xA9] = 'z'

d[0xC0] = '{'
d[0xC1] = 'A'
d[0xC2] = 'B'
d[0xC3] = 'C'
d[0xC4] = 'D'
d[0xC5] = 'E'
d[0xC6] = 'F'
d[0xC7] = 'G'
d[0xC8] = 'H'
d[0xC9] = 'I'

d[0xD0] = '}'
d[0xD1] = 'J'
d[0xD2] = 'K'
d[0xD3] = 'L'
d[0xD4] = 'M'
d[0xD5] = 'N'
d[0xD6] = 'O'
d[0xD7] = 'P'
d[0xD8] = 'Q'
d[0xD9] = 'R'

d[0xE0] = '\\'
 
d[0xE2] = 'S'
d[0xE3] = 'T'
d[0xE4] = 'U'
d[0xE5] = 'V'
d[0xE6] = 'W'
d[0xE7] = 'X'
d[0xE8] = 'Y'
d[0xE9] = 'Z'

d[0xF0] = '0'
d[0xF1] = '1'
d[0xF2] = '2'
d[0xF3] = '3'
d[0xF4] = '4'
d[0xF5] = '5'
d[0xF6] = '6'
d[0xF7] = '7'
d[0xF8] = '8'
d[0xF9] = '9'
d[0xFA] = '|'

keyw = '*/.'

while True:
    text  = ''
    bytes = ifile.read(record_len)
    for j in range(record_len):
       text  = text  + d[bytes[j]]
    print(text)
    ofile.write(text + '\n')   
    if keyw in text:
       break 
   
ifile.close()
ofile.close()

exit()
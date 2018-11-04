gl_ok=['у','ю','ешь','ет', 'ем', 'ете', 'ут','ют','ишь','ит','им','ите','ат','ят','ить','иться','ать','ется','аться','оть','оться','ень','ай']
zn='.!,?:;-"'


file1=open("rifm","r")
text1=file1.read()
file1.close()
glasn='уёеыаоэяию'
text11=''
for i in text1:
    if i not in zn:
        text11+=i

text1=text11.lower()
del(text11)
text3=[]
text2=text1.split('\n')
for i in text2:
    text3+=i.split(' ')


glagols=[]
for i in text3:
    for j in gl_ok:
        if len(i)>len(j)+1 and j in i and i not in glagols and i!=' ' and i!='':
            glagols.append(i)

def rifm(old1,text,slog):
    op2=True
    while op2:
                ngl1=texr[random.randint(1,len(text)-1)]
                if ngl1[-1:]==old[-1:]and old!=ngl1:
                    op2=False
    return ngl1

import random
file1=open('glag','w')

ngl=glagols[random.randint(1,len(glagols)-1)]
kgl = text3[random.randint(1,len(text3)-1)]
mgl = text3[random.randint(1,len(text3)-1)]
slog=0
for i in ngl+kgl+mgl:
    if i in glasn:
        slog+=1
for i1 in range(3):
    for i in range(4):
        slog1=0
        while not (slog+2>slog1 and slog-1<slog1):
            op2=True
            slog1=0
            while op2:
                ngl1=glagols[random.randint(1,len(glagols)-1)]
                if ngl1[-1:]==ngl[-1:]and ngl!=ngl1:
                    op2=False
            op2=True
            while op2:
                mgl1 = text3[random.randint(1,len(text3)-1)]      
                if mgl1[-2:]==mgl[-2:]and mgl!=mgl1:
                    op2=False
            op2=True
            while op2:
                kgl1 = text3[random.randint(1,len(text3)-1)]      
                if kgl1[-1:]==kgl[-1:]and kgl!=kgl1:
                    op2=False
            for i in ngl1+kgl1+mgl1:
                if i in glasn:
                    slog1+=1
        file1.write(kgl1+' '+str(ngl1)+' '+mgl1+'\n')
    file1.write('\n')


file1.close()
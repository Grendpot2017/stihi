gl_ok=['у','ю','ешь','ет', 'ем', 'ете', 'ут','ют','ишь','ит','им','ите','ат','ят','ить','иться','ать','ется','аться','оть','оться','ень','ай']
pr_ok=[]
zn='.!,?:;-"'
mest=['я','ты','он','она','оно','мы','вы','они','Вы','ты','я','ты']
predlog=['в','от','на','не','под','над','от','до','с','во','вот','и','или']

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
        if len(i)>len(j)+1 and j==i[-len(j):] and i not in glagols and i!=' ' and i!='':
            glagols.append(i)

def rifm(old1,text,slog,l,textnot):
    op2=True
    if len(old1)>1:
        if old1[-1]=='':
            ngl1=text[random.randint(0,len(text)-1)]
    else:
        while op2:
            ngl1=text[random.randint(1,len(text)-1)]
            if ((len(old1)>1 and ngl1[-l:]==old1[-1][-l:]and old1[-1]!=ngl1) or(len(old1)==1 and ngl1[-l:]==old1[0][-l:]and old1[0]!=ngl1)) and not(ngl1 in textnot) and not (ngl1 in old1):
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
    ng=[ngl]
    kg=[kgl]
    mg=[mgl]
    for i in range(4):
        slog1=0
        l1=0
        
        kg=list()
        mg=list()
        while not (slog+2>slog1 and slog-1<slog1):
            op2=True
            slog1=0
            pr=rifm('',mest,slog,0,'')
            ngl1=rifm(ng,glagols,slog,1,'')
            mgl1=rifm(mg,text3,slog,1,glagols+predlog)
            kgl1=rifm(kg,text3,slog,1,glagols+predlog)
            for i in ngl1+kgl1+mgl1+pr:
                if i in glasn:
                    slog1+=1
        file1.write(pr+' '+kgl1+' '+str(ngl1)+' '+mgl1+'\n')
        kgl=kgl1
        mgl=mgl1
        ngl=ngl1
        ng.append(ngl)
        mg.append(mgl)
        kg.append(kgl)
    file1.write('\n')
file1.close()
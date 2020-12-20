import os


def mfolder(allfolder,basenames,basefolder,errorfolder):
    for basename in basenames:
        for alls in allfolder:
            if alls[-4:]==basename+'.m':
                basefolder[basename][alls]=[]
            elif alls[-5:]==basename+'.m':
                basefolder[basename][alls]=[]
    for basename in basenames:
        for var in basefolder[basename]:
            try:
                f = open('..\\'+'sourse\\'+var,'r+',encoding="utf-8")
                basefolder[basename][var] = f.read()
                f.close()
            except:
                errorfolder.append([basename,var])
    for vb in errorfolder:
        
        try:
            f = open('..\\'+'sourse\\'+vb[1],'r+',encoding="gbk")
            basefolder[vb[0]][vb[1]] = f.read()
            f.close()
            errorfolder.remove(vb)
        except:
                ghkfjfghjfg=1
    for vb in errorfolder:
        
        try:
            f = open('..\\'+'sourse\\'+vb[1],'r+',encoding="big-5")
            basefolder[vb[0]][vb[1]] = f.read()
            f.close()
            errorfolder.remove(vb)
        except:
                ghkfjfghjfg=1
    for vb in errorfolder:
        
        try:
            f = open('..\\'+'sourse\\'+vb[1],'r+',encoding="gb18030")
            basefolder[vb[0]][vb[1]] = f.read()
            f.close()
            errorfolder.remove(vb)
        except:
                ghkfjfghjfg=1
 #   return names
    
    
def getFiles(sourse): # 查找根目录，文件后缀 
    L=[]
    for root, dirs, files in os.walk(sourse):  
            for file in files:  
                if os.path.splitext(file)[1] == '.m':  
                    c=os.path.join(root, file)
                    d=len(sourse)
                    L.append(c[d+1:]) 
    return L
def bijiao(fd0,fd1,zong_hang,xiangsi_hang):
    ret=[]
    f0_bh=[]
    f0_val=[]
    for i in fd0:
        f0_bh.append(i[0])
        f0_val.append(i[1])
    f1_bh=[]
    f1_val=[]
    for i in fd1:
        f1_bh.append(i[0])
        f1_val.append(i[1])
    n0=len(fd0)
    n1=len(fd1)
    for ii in range(0,n0-zong_hang):
        for jj in range(0,n1-zong_hang):
            fg0s=f0_val[ii:zong_hang+ii]
            fg1s=f1_val[jj:zong_hang+jj]
            jh=0
            for fg0 in fg0s:
                if fg0 in fg1s:
                    jh+=1
            if jh>=xiangsi_hang:
                ret.append([f0_bh[ii],f0_bh[zong_hang+ii-1],f1_bh[jj],f1_bh[zong_hang+jj-1]])
                
    return ret



def find_name_error(folder,m_name):
    L=[]
    for fn in folder:
        i=0
        for v in m_name:
            if v in fn:
                i=1
        if i==0:
            L.append(fn)
    return L
        










    
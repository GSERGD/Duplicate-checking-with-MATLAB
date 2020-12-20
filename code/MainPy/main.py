import os
from loadfolder import *
from RemoveStr import Handle 
import xlwt

errorfolder=[]

basenames=['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21']
basenames_allname=[]
for x123 in basenames:
    basenames_allname.append(x123+'.m')
    for fnj in range(0,10):
        basenames_allname.append(x123+'_'+str(fnj)+'.m')
sourse=os.path.abspath('..')+'\sourse'
print('根目录:'+sourse)
basefolder={}
yuanshiwenjian={}
for i in basenames:
    basefolder[i]={}
allfolder=getFiles(sourse)
mfolder(allfolder,basenames,basefolder,errorfolder)
#命名错误
name_error=find_name_error(allfolder,basenames_allname)
#

#copy
for i in basenames:
    yuanshiwenjian[i]={}
allfolder=getFiles(sourse)
mfolder(allfolder,basenames,yuanshiwenjian,errorfolder)
# =============================================================================
#去除无效字符
qu_str=';: '

qu_keys=['if','while','sum']
key_bianmas=['00000001','0000010','00000100',]

hd=Handle(basefolder)
hd.removeStrs(qu_str)

hd.yuchuli()
# =============================================================================

           
# =============================================================================
# 查重
result=[]
zong_hang=8
xiangsi_hang=5
chuli_folder=hd.basefolder
for Q,value in chuli_folder.items():
    allnames=[]
    allfolder=[]
    for names,val in value.items():
        if val!=[]:
            asd=list(names)
            allnames.append("".join(asd[:]))
            allfolder.append(val)
    len_all=len(allnames)
    for i in range(0,len_all-1):
        if len(allfolder[i])<zong_hang:
                continue
        for j in range(i+1,len_all):
            
            if len(allfolder[j])<zong_hang:
                continue
            fd0=allfolder[i]
            fd1=allfolder[j]
            result01=bijiao(fd0,fd1,zong_hang,xiangsi_hang)  #在loadfolder
            if result01!=[]:
                result.append([Q,allnames[i],allnames[j],result01])
# =============================================================================

# =============================================================================
# 人工复查



fucha=0




total=0
n_now=0

judge=[]
final_result=[]
yuzhi=1.5
for x in result:
   # try:
                pe1=yuanshiwenjian[x[0]][x[1]]
                pe2=yuanshiwenjian[x[0]][x[2]]

                
                pe1_list=pe1.split('\n')
                pe2_list=pe2.split('\n')
                n1=len(pe1_list)
                n2=len(pe2_list)
                n0=0
                if n1>n2:
                    n0=n1
                    koi=n1*1.0/n2
                else:
                    n0=n2
                    koi=n2*1.0/n1
                if koi<yuzhi:
                    total+=1
if fucha==1:
    for x in result:
                pe1=yuanshiwenjian[x[0]][x[1]]
                pe2=yuanshiwenjian[x[0]][x[2]]

                pe1_list=pe1.split('\n')
                pe2_list=pe2.split('\n')
                n1=len(pe1_list)
                n2=len(pe2_list)
                n0=0
                if n1>n2:
                    n0=n1
                    koi=n1*1.0/n2
                else:
                    n0=n2
                    koi=n2*1.0/n1
        
                    
                
                if koi<yuzhi:
                    n_now=n_now+1
                    final_result.append(x)
                    for i in range(0,n0):
                        print(str(i)+'   ',end='')
                        if i<n1:
                            print("|",pe1_list[i].ljust(100),end='')
                        else:
                            print("|",' '.ljust(100),end='')
                        if i<n2:
                            print("|",pe2_list[i].ljust(100))
                        else:
                            print("|",' '.ljust(100))
                    print(x[3])
                    print('%d/%d  '%(n_now,total),end='')
                    c=input('请输入复查结果,抄袭为1,不抄袭为0:')
                    c0=list(c)
                    
                    if '1' in c0:
                        judge.append('1')
                    else:
                        judge.append('0')
# =============================================================================



# =============================================================================
# 保存
# 创建一个workbook 设置编码
if 1:
    workbook= xlwt.Workbook(encoding = 'utf-8')
    # 创建一个worksheet
    final_worksheet = workbook.add_sheet('Final')
    nameerror11=workbook.add_sheet('NameError')
    original_worksheet = workbook.add_sheet('Original')
    Openfailed_worksheet=workbook.add_sheet('OpenFailed')
    nfail=0
    for kud in errorfolder:
        Openfailed_worksheet.write(nfail,0, label = kud[0])
        Openfailed_worksheet.write(nfail,1, label = kud[1])
        nfail=nfail+1
    nne=0
    for erre in name_error:
        nameerror11.write(nne,0, label = erre)
        nne=nne+1
    # 写入excel
    # 参数对应 行, 列, 值
    npeople=0
    nn=0
    nname=0
    for x in final_result:
        na1=x[1]
        na2=x[2]
        name11=''
        name22=''
        for h1 in list(na1):
            if h1!=')':
                name11=name11+h1
            else:
                break
        for h2 in list(na2):
            if h2!=')':
                name22=name22+h2
            else:
                break
        
        original_worksheet.write(npeople,0, label = x[0])
        original_worksheet.write(npeople,1, label =name11+')')
        original_worksheet.write(npeople,2, label =name22+')')
        
        if judge[npeople]=='1':
            if fucha==1:
                final_worksheet.write(nn,0, label = x[0])
                final_worksheet.write(nn,1, label =name11+')')
                final_worksheet.write(nn,2, label =name22+')')
                nn=nn+1
        npeople=npeople+1
        
    
    # 保存
    workbook.save('../result/result.xls')
# =============================================================================
print('\n\n查重完成\n\n')


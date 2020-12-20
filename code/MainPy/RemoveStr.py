

class Handle():
    def __init__(self,basefolder):
        self.basefolder=basefolder
        self.zimu=list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_')
        self.shuzi=list('0123456789')
        self.zifu=list('`!~@#$%^&*()_+-=[]\;,./{}|:<>?'+'"'+"'"+'+-*/')
        self.zimushuzi=list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_0123456789')
    def removeStrs(self,removestr):
        removelist=list(removestr)
        for Qs,value in self.basefolder.items():
            for name,val in value.items():
                if val != []:
                    val_list=list(val)
                   
                    for rmv in removelist:
                        while rmv in val_list:
                            val_list.remove(rmv)
                    self.basefolder[Qs][name]="".join(val_list)
    def yuchuli(self):
        for Qs,value in self.basefolder.items():
            for name,val in value.items():
                if val != []:
                    
                    val=val.split("\n")
                    i=0
                    kong=[]
                    for hang in val:
                        hang=self.hang_chuli(hang)
                        i+=1
                        if hang!='end':
                            if hang!='':
                                kong.append([i,[hang]])
                    self.basefolder[Qs][name]=kong
    def hang_chuli(self,hang):
        rslt=[]
        hang_list=list(hang)
        j_zimu=0
        j_shuzi=0
        for hstr in hang_list:
            
            if hstr in self.zimu:
                if j_zimu==0:
                    #rslt.append('a')
                    #j_zimu=1
                    aaaaaaaa=0
            elif hstr in self.shuzi:
                if j_zimu==1:
                    gregrgeg=0
                else:
                    if j_shuzi==0:
                       rslt.append('2') 
                       j_shuzi=1
            elif hstr in self.zifu:
                rslt.append(hstr) 
                j_zimu=0
                j_shuzi=0
        #return "".join(rslt)
        return hang
    
    

        
        
        
        
        
operators=['v','^','~']
def not_eval(s,f=None):
    try:
        if f==None: f=s.index('~')                
        if s[f+1]=='~':s[f:f+2]=''
        elif s[f+1]=='v': s[f : f+2]='^'
        elif s[f+1]=='^': s[f:f+2]='v'    
        s[f+2:]=not_eval(s[f+2:])
        return s    
    except ValueError:               
        return s

def move_not_inwards(s):
    try:
        s=list(s)
        f=s.index('~')
        if s[f+1]=='(':
            s[f],f,flag='',f+2,False           
            while s[f]!=')':
                if s[f] in operators: flag=True        
                if s[f]!='(':
                    s.insert(f,'~')  
                    s=not_eval(s,f)
                    f=f+s[f:].index(')')+1 if not flag else f+1
                else:     
                    s.insert(f,'~')
                    s[f:],f1=list(move_not_inwards(s[f:]))
                    f=f1+f
                flag=False
            return s,f    
        else: return not_eval(s,f),f    
    except ValueError:        
        return s,len(s)

def move_not_expression(s):
    s=list(s.strip())
    try:
        f=0
        while True:
            s[f:],f1=move_not_inwards(s[f:])
            if s[f:] == []: raise ValueError()
            f=f+f1
            if f==f1+f: f+=1
    except ValueError:
        return ''.join(s)

def eliminate_single_implication(s,f):
    try:
        pos=f
        f-=3
        d=1
        while d!=0 or f>0:
            if d==0 and s[f]=='(': break    
            if s[f]==')': d+=1
            if s[f]=='(':d-=1      
            f-=1
        s.insert(pos-1,')')
        s.insert(f+1,'~')
        s.insert(f+2,'(')
        s[pos+2:pos+4]='v'
        return s,pos+4
    except ValueError:
        return s,f    

def eliminate_double_implication(s,f):
    try:
        l1,r1,l2,r2,d=f-2,f,f+3,f+4,1
        if s[l1]!=')':l1=-1
        if(s[l2+1]!='(') : r2=len(s)    
        while d!=0 or s[l1] not in operators:
            if l1<0: break
            if s[l1]==')': d+=1
            if s[l1]=='(':d-=1
            l1-=1
        l1,d=l1+1,1    
        while d!=0 or s[r2] not in operators:
            if r2>=len(s): break  
            if s[r2]==')':d+=1
            if s[r2]=='(':d-=1
            r2+=1       
        s[l1:r2]=['(']+s[l1:r1]+list('->')+s[l2:r2]+[')']+list('^')+['(']+s[l2:r2]+list('->')+s[l1:r1]+[')']                   
        return s,r2
    except ValueError:    
        return s,f     

def eliminate_implication(s):
     s=list(s.strip())
     try:
        f=-1
        while True:    
            f=s.index('<',f+1) 
            s,f=eliminate_double_implication(s,f)
     except ValueError:
         f=-1
         try:
            print(''.join(s)) 
            while True:
                f=s.index('>',f+1)
                s,f=eliminate_single_implication(s,f)
         except ValueError:
             print(''.join(s))
             return ''.join(s)

def solve(s):
    s=eliminate_implication(s)
    return move_not_expression(s)
    
print(solve('A(x)^B(x)^person(x)^bad(x)->likes(x,pizza)^asom(x)'))


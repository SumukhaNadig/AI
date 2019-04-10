def read_data_hash():
    f=open('hash_data.txt','r')
    s=f.readlines()
    f.close()
    maze=[]
    st,e=(0,0),(0,0)
    f,g=False,False
    for i in range(len(s)): 
        s[i]=s[i].replace('#','0').replace(' ','1').replace('\n','')
        if not f and 's' in s[i]: 
            st,f=(i,s[i].index('s')),True
        if not g and 'e' in s[i]:
             e,g=(i,s[i].index('e')),True    
        maze.append([int(x) if x!='s' and x!='e' else x for x in s[i]])
    print('-'*10+'data loaded'+'-'*10)    
    return maze,st,e    

   








prep=input("Enter the preposition logic:       ")
di=prep.find('<=>')
prep=prep[0:di]+"=>"+prep[di+3:len(prep)]+" ^ "+prep[di+3:len(prep)]+"=>"+prep[0:di]
print("\n1.Removing double implies:      "+prep)
i=prep.find('=>')
while(i!=-1):
    if prep[i-1]!=")":
        prep=prep[0:i-1]+"!"+prep[i-1]+" v "+prep[i+2:]
    else:
        '''ib=prep.find('(')'''
        j=i
        while prep[j]!='(':
            j-=1
        prep=prep[0:j]+"!"+prep[j:i]+" v "+prep[i+2:]    
    i=prep.find('=>')
print("\n2.Removing single implies:      "+prep)
n=prep.find('!(')
while(n!=-1):
    if prep[n+1]=='(':
        prepn=prep
        prep=prepn[0:n+1]
        i=n+2
        while(prepn[i]!='^' and prepn[i]!='v'):
            if(prepn[i]!='('):
                prep+=prepn[i]
            i+=1
        if prepn[i]=='^':
            prep+=' v '
        elif prepn[i]=='v':
            prep+=' ^ '
        prep+='!'+prepn[i+1:prepn.find(')',i)]
        prep+=prepn[prepn.find(')',i)+1:]
    n=prep.find('!(')
print("\n3.Demorgan's Law:               "+prep)

dn=prep.find('!!')
while(dn!=-1):
    prep=prep[:dn]+" "+prep[dn+2:]
    dn=prep.find('!!')
print("\n4.Removing double negation:     "+prep)

prepn=prep
prep=""
for i in prepn:
    if i!='(' and i!=')':
        prep+=i
print("\n5.Removing unwanted brackets:   "+prep)

prepn=prep
prep="("
for i in prepn:
    if i=='^':
        prep+=') ^ ('
    else:
        prep+=i
prep+=')'
print("\n6.Grouping into CNF form:       "+prep)
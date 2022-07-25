ch= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g","a", "x", "a"]
i=0
a=[]
while i<len(ch):
    p=ch[i]
    j=0
    s=0 
    while j<=i:
       k=ch[j]
       j=j+1
       if p==k:
           s=s+1       
    if s==1:
        a.append(p)        
    i=i+1      
t=0
while t<len(a):
    d=a[t]
    c=0
    chsum=0
    while c<len(ch):
            f=ch[c] 
            c=c+1
            if d==f:
                chsum=chsum+1
    t=t+1            
    print(d,"=",chsum)           
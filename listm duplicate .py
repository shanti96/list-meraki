n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
a=[]
i=0
while i <len(n):
    p=n[i] 
    j=0
    s=0
    while j<=i:
        k=n[j]
        j=j+1
        if p==k:
            s=s+1
    if s==1:    
        a.append(p) 
    i=i+1
print("duplicate number=",a)
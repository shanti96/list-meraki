number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
while i<len(n):
    p=n[i]
    j=i+1
    while j<len(n):
        a=n[j]
        b=p+a
        j=j+1 
        if b==number:
            c=(p,a)
            print(list(c),end=",")     
    i=i+1   
num =[1, 1, 0,1,]
n=-1
sum=0
a=-1
j=1
while n>=-len(num):
    p=num[n]
    if p==1 or p==0:            
       n=n-1       
    else:
        print("not correct number")
        break
    while a>=-len(num):
        b=num[a]
        if b==1:
             sum=sum+j
        j=j*2 
        a=a-1  
print(sum)        
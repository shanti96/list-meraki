name=[ '1','2','2','2' ]
i=-1
j=''
while i>=-len(name):
    n=name[i]
    j=j+n
    i=i-1
a=0    
c=""
while a<len(name):
    b=name[a]
    c=c+b
    a=a+1    
if c==j:
    print('pallindrome')
else:
    print("not pallindrome")    

#pallindrome
name=[ 'n', 'i', 't', 'i', 'n' ]
rev=name[::-1]
if name==rev:
    print("pallindrome",rev)
else:
    print("not")        
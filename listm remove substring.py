a= "the quick brown fox jumped over the lazy dog .the dog slept over the verandah."
b=a.split()
c=''
i=0
while i<len(b):
    if b[i]=='over':
        c=c+" "+'on'
        i=i+1
    c=c+" "+ b[i]    
    i=i+1
print(c)        
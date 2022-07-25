elem = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42,2, 43]
i=0
e=0
o=0
even=0
odd=0
while i<len(elem):
    p=elem[i]
    if p%2==0:
        e=e+1
        even=even+p
    elif p%2!=0:
        o=o+1
        odd=odd+p
    i=i+1    
print("total average of even number=",even//e) 
print("total average of odd number=",odd//o)           
number=[50, 40, 23, 70, 56, 12, 5, 10, 7]
numlen=len(number)
index=0
p=0
while index<numlen:
    n=number[index]
    if n>=20 and n<=40:
        p=p+1
    index=index+1
print("total number between 20 to 40=", p)    
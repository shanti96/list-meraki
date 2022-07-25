num=[50, 40, 23, 70, 56, 12, 5, 33, 10, 7]
i=0
n=0
while i<len(num):
    index=num[i]
    if index>=20 and index<=50:
        n=n+1
    i=i+1
print(n)    
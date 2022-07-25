num = [50, 40, 23, 70, 56, 12, 5, 7]
m=0
i=0
while i<len(num):
    if num[i]>m:
       m=num[i]
    i=i+1
sm=0
j=0
while j<len(num):
    if num[j]>sm and num[j]!=m:
        sm=num[j]
    j=j+1
tm=0
k=0
while k<len(num):
    if num[k]>tm and num[k]<sm and num[k]!=m:
        tm=num[k]
    k=k+1
print("max number=",m)
print("second max number=",sm) 
print("third max number=",tm)                      
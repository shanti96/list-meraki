a=[1,2,2,3,4,4,4,5]
b=[i for i in a if a.count(i)>1]
print(b)
c=set(b)
print(c)
d=list(c)
print(d)
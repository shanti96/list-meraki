list1 = [1,2,3,8,4,5]
list2 = [2,3,1,0,6]
n=0
while n<len(list1):
    p=list1[n]
    j=0
    while j<len(list2):
        k=list2[j]
        j=j+1
        if p==k:
            break 
    else:
        print(p) 
    n=n+1                 
marks = [[78, 76, 94, 86, 88],
        [91, 71, 98, 65, 76],
        [95, 45, 78, 52, 49]]
n=len(marks)
sum=0
i=0
while i<n:
    p=0
    while p<len(marks[i]):
        j=marks[i][p]
        sum=sum+j
        p=p+1    
    i=i+1    
print(sum)    
marks = [[78, 76, 94, 86, 88],
        [91, 71, 98, 65],
        [95, 45, 78]]
n=len(marks)
i=0
year=1
while i<n:
    p=0
    sum=0
    while p<len(marks[i]):
        j=marks[i][p]
        sum=sum+j
        p=p+1
    a=sum//len(marks[i])
    print("average of",year,"year=",a)
    year=year+1
    i=i+1    
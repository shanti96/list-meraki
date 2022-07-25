magic_square = [[8,3,4],[1,5,9],[6,7,2]]
i=0
row=0
while i<len(magic_square): 
    p=0 
    while p<len(magic_square[i]):
        j=magic_square[i][p]
        row=row+j
        p=p+1    
    i=i+1    
i=0
colom=0
while i<len(magic_square):
    p=0
    while p<len(magic_square[i]):
        j=magic_square[p][i]
        colom=colom+j
        p=p+1
    i=i+1   
i=0
digonal=0
while i<len(magic_square):
    p=i
    while p<len(magic_square[i]):    
      j=magic_square[p][p]
      digonal=digonal+j
      p=p+len(magic_square[i])
    i=i+1    
i=-1
n=0
digonal2=0
while i>=-len(magic_square):
    p=i
    while p>=-len(magic_square[n]):
        j=magic_square[n][i]
        digonal2=digonal2+j
        p=p-len(magic_square[i])
    n=n+1    
    i=i-1    
if row==colom and digonal==digonal2:
    print("valid magic square")  
else:
    print("not magic square")    
x=len(magic_square)    
print(row//x,colom//x,digonal,digonal2)          
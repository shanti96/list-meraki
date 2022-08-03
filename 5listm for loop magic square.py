# list=['A','A','B','C','A','B','C']
# a=list.count('A')
# print(a)
# list.clear()
# print(list) 

#magic square#
a=[[8,3,4],[1,5,9],[6,7,2]] 
for i in range(0,len(a)):
    col=0
    for j in range(0,len(a)):
        col=col+a[j][i]
    print(col)    
    row=0
    for k in range(0,len(a)): 
        row=row+a[i][k]
    print(row)    
    digonal=0
for n in range(0,len(a)):
    digonal=digonal+a[n][n]
re_digonal=0
f=0
for p in range(-1,-(len(a)+1),-1):
    re_digonal=re_digonal+a[p][f] 
    f=f+1
print(re_digonal)    
#print("colom=",col,"row=",row,"digonal=",digonal,"re_digonal=",re_digonal) 
if col==row and row==digonal and digonal==re_digonal:
    print("valid magic square")
else:
    print("not valid")    
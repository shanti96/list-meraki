# a=["shantipriya"]
# vo=''
# co=''
# for i in range(0,len(a[0])):
#     c=a[0][i]
#     if c=='a'or c=='e'or c=='i'or c=='o'or c=='u':
#         vo=vo+c
#     else:
#         co=co+c    
# print('vowel=',vo,",",'consonant=',co)  
# 
 
a="welcome 39 to 3 navgurukul 2016"  
b=''
for i in range(0,len(a)):
    c=a[i]
    if 'a'<=c and 'z'>=c or " "==c:  
       b=b+c
print(b)    
d=b.split()
print(d) 
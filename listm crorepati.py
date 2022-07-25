kitna_paisa= [3000, 600000, 324990909, 90990900, 30000, 
            5600000, 690909090, 31010101, 532010, 510, 4100]
crorepati=0
lakhpati=0
dilwale=0    
i=0
while i<len(kitna_paisa):
    n=kitna_paisa[i]
    i=i+1
    if n>=10000000:
        crorepati=crorepati+1
    elif n<10000000 and n>=100000:
        lakhpati=lakhpati+1
    else:
        dilwale=dilwale+1
print("crorepati=",crorepati,"lakhpati=",lakhpati,"dilwale=",dilwale)                               
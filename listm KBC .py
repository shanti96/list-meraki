queation=["What is the capital of India?","NG mei kaun se course padhaya jaata hai?","How many continents are there?"]
option=[["1. Chandigarh" ,"2. Bhopal" ,"3. Chennai","4. Delhi"],["1.Software Engineering", "2.Counseling", "3.Tourism ","4.Agriculture"],["1.Four"," 2.Nine" ," 3.Seven" ," 4.Eight"]] 
answer=[4,1,3]   
_5050=[["3. Chennai","4. Delhi"],["1.Software Engineering", "2 Counseling"],[" 3.Seven" ," 4.Eight"]]   
k=0
i=0
rupe=0
while i<len(queation):
    n=i 
    while n==i:
        print(queation[i]) 
        n=n+1
        j=0
        while j<len(option[i]):
            print(option[i][j])
            j=j+1    
        m=k    
        while m<1:
            lifeline=input("do you want life line")
            m=m+1
            if lifeline=="yes":
                k=1
                s=0
                while s<len(_5050[i]):
                    print(_5050[i][s])
                    s=s+1      
    select=int(input("choise any one option")) 
    if select==answer[i]:
        rupe=rupe+1000
        print("Congrats! Aapka answer sahi hai")
        print("you win=",rupe)
    else:
        print("Sadly aapka javab ga1lat hai. out of the game now.") 
        break               
    i=i+1    
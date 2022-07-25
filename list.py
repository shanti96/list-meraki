name=["nani",9,"sita",1.2]
name[0]=1.0
name.pop()
name.append("rohit")
print(name)
print(type(name))
print(name[3])

marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
total_marks = 0
counter = 0 
while counter < len(marks):
 total_marks = total_marks + int(marks[counter])
 counter = counter + 1
print(total_marks) 
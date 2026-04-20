# program that stores records of students who won competitions. 

n = int(input("enter number of students: "))

CompWinner = { }

for a in range(n):
    key = input("name of the student: ")
    value = int(input("number of competitions won: "))
    
    CompWinner[key] = value

print("the dictionary now is: ")
print(CompWinner)

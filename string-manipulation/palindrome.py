# program that checks whether a string is palindrome or not.

string = input("enter a string: ")
length = len(string)

rev = -1

for i in range(length // 2):
    if string[i] == string[rev]:
        rev -= 1  # index moving backward
    else: 
        print("not palindrome")
        break    
else:
    print("palindrome")    
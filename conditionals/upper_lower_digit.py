ch = input("enter a single character: ")

if ch >= 'A' and ch <= 'Z':
    print("you entered a UPPER case character")

elif ch >= 'a' and ch <= 'z':
    print("you entered a LOWER case character")

elif ch >= '0' and ch <= '9':
    print("you entered a digit")
else:
    print("you entered a special character")            
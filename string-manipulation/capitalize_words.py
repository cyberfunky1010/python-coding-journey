# program to take a string as input and capitalize the first letter of each word in the string and make a new string out of it.
# basic idea is that to solve : if there is a space before the current character then capitalize it otherwise just add it to the new string.

string = input("Enter a string: ")
len = len(string)
new_string = ""

for i in range(len):
    if i == 0:                                # capitalize the first letter of the string even if there is space. 
        new_string = new_string + string[0].upper()  
    elif string[i-1] == " ":                 # if the previous character is space that means current character is the first letter of the word so capitalize it
        new_string = new_string + string[i].upper()
    else:                                   # if its nether the first character nor coming after a space just add character in it. 
        new_string = new_string + string[i]

print("Capitalized string: ", new_string)

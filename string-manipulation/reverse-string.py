# program to display reversed string. not acutally reversing a string.

string1 = input("enter string to reverse: ")
length = len(string1)
print("word",string1,"in reverse order is ")

for a in range(-1,(-length-1),-1): #or (length-1,-1,-1) - this is more readable
    print(string1[a])
    
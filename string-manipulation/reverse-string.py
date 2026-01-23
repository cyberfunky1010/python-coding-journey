# program to display reversed string. not acutally reversing a string.

string1 = input("enter string to reverse: ")
length = len(string1)
print("word",string1,"in reverse order is ")

for a in range(-1,(-length-1),-1): #or (length-1,-1,-1) - this is more readable
    print(string1[a])
    
# same program with printing stirng in order and in reverse.

string2 = input("enter string: ")
length = len(string2)
i = 0
for a in range(length-1,-1,-1):
    print(string2[i],"\t",string2[a])
    i+=1

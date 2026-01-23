string1 = input("enter string to reverse: ")
length = len(string1)
print("word",string1,"in reverse order is ")

for a in range(-1,(-length-1),-1):
    print(string1[a])
# program to count frequency of a given element in a list of numbers. 

lst = eval(input("enter list: "))
length = len(lst)

element = int(input("enter element: "))
count = 0

for i in range(length):
    if element == lst[i]:
        count += 1
if count == 0:
    print(element,"not found in the list")        
else:
    print(element, "has frequency of", count)     


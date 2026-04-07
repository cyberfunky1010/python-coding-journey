# program to search for an element in a given list of numbers. 

lst = eval(input("enter list: "))
length = len(lst)

element = int(input("enter element to find: "))

for i in range(length):
    if element == lst[i]:
        print(element,"found at index",i)
        break
else:
    print(element,"not found in the list")
